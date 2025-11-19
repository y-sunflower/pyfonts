import pytest
from matplotlib.font_manager import FontProperties
from pyfonts import load_bunny_font
from pyfonts.utils import _get_fonturl
from pyfonts.is_valid import _is_url, _is_valid_raw_url


def test_errors():
    with pytest.raises(ValueError, match="`weight` must be between 100 and 900"):
        _get_fonturl(
            endpoint="https://fonts.bunny.net/css",
            family="Roboto",
            weight=90,
            italic=False,
            allowed_formats=["woff", "ttf", "otf"],
            use_cache=False,
        )

    with pytest.raises(RuntimeError, match="No font files found in formats"):
        _get_fonturl(
            endpoint="https://fonts.bunny.net/css",
            family="Roboto",
            weight=400,
            italic=False,
            allowed_formats=["aaa"],
            use_cache=False,
        )


@pytest.mark.parametrize("family", ["Alumni Sans", "Roboto"])
@pytest.mark.parametrize("weight", [None, 300, 800])
@pytest.mark.parametrize("italic", [None, True, False])
def test_get_fonturl(family, weight, italic):
    url = _get_fonturl(
        endpoint="https://fonts.bunny.net/css",
        family=family,
        weight=weight,
        italic=italic,
        allowed_formats=["woff", "ttf", "otf"],
        use_cache=False,
    )

    assert isinstance(url, str)
    assert _is_url(url)
    assert _is_valid_raw_url(url)


@pytest.mark.parametrize("family", ["Roboto", "Open Sans"])
@pytest.mark.parametrize("weight", [None, 300, 500, 800, "bold", "light", "regular"])
@pytest.mark.parametrize("italic", [None, True, False])
@pytest.mark.parametrize("use_cache", [True, False])
def test_load_bunny_font(family, weight, italic, use_cache):
    font = load_bunny_font(family, weight=weight, italic=italic, use_cache=use_cache)

    assert isinstance(font, FontProperties)
    assert font.get_name() == family


def test_weird_api_error():
    with pytest.raises(ValueError, match="No font available for the request at URL*"):
        load_bunny_font("Alice", italic=True)
