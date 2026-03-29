import pytest
from matplotlib.font_manager import FontProperties
from pyfonts import load_google_font
from pyfonts.utils import _get_fonturl
from pyfonts.is_valid import _is_url, _is_valid_raw_url


def test_errors():
    with pytest.raises(ValueError, match="`weight` must be between 100 and 900"):
        _get_fonturl(
            endpoint="https://fonts.googleapis.com/css2",
            family="Roboto",
            weight=90,
            italic=False,
            allowed_formats=["woff2", "woff", "ttf", "otf"],
            use_cache=False,
        )

    with pytest.raises(RuntimeError, match="No font files found in formats"):
        _get_fonturl(
            endpoint="https://fonts.googleapis.com/css2",
            family="Roboto",
            weight=400,
            italic=False,
            allowed_formats=["aaa"],
            use_cache=False,
        )


@pytest.mark.parametrize("family", ["Roboto", "Open Sans"])
@pytest.mark.parametrize("weight", [300, 500, 800])
@pytest.mark.parametrize("italic", [True, False])
def test_get_fonturl(family, weight, italic):
    url = _get_fonturl(
        endpoint="https://fonts.googleapis.com/css2",
        family=family,
        weight=weight,
        italic=italic,
        allowed_formats=["woff2", "woff", "ttf", "otf"],
        use_cache=False,
    )

    assert isinstance(url, str)
    assert _is_url(url)
    assert _is_valid_raw_url(url)


@pytest.mark.parametrize("family", ["Roboto", "Open Sans"])
@pytest.mark.parametrize("weight", [300, 500, 800, "bold", "light", "regular"])
@pytest.mark.parametrize("italic", [True, False])
@pytest.mark.parametrize("use_cache", [True, False])
def test_load_google_font(family, weight, italic, use_cache):
    font = load_google_font(family, weight=weight, italic=italic, use_cache=use_cache)

    assert isinstance(font, FontProperties)
    assert font.get_name() == family


def test_get_fonturl_subset_nonexistent_falls_back(monkeypatch):
    css = (
        "/* latin */\n@font-face { src: url(https://example.com/font-latin.woff2); }\n"
    )

    class DummyResponse:
        text = css

        def raise_for_status(self):
            return None

    monkeypatch.setattr("pyfonts.utils.requests.get", lambda _: DummyResponse())

    url = _get_fonturl(
        endpoint="https://fonts.googleapis.com/css2",
        family="Roboto",
        weight=400,
        italic=False,
        allowed_formats=["woff2"],
        use_cache=False,
        subset="this-subset-does-not-exist",
    )

    assert url == "https://example.com/font-latin.woff2"
