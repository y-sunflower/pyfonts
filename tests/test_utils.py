from pyfonts.utils import _get_fonturl, _map_weight_to_numeric, _parse_css_subsets
import pytest


def test_parse_css_subsets_multi():
    css = (
        "/* thai */\n"
        "@font-face { src: url(https://example.com/font-thai.woff); }\n"
        "/* latin */\n"
        "@font-face { src: url(https://example.com/font-latin.woff); }\n"
        "/* latin-ext */\n"
        "@font-face { src: url(https://example.com/font-latin-ext.woff); }\n"
    )
    result = _parse_css_subsets(css)
    assert "thai" in result
    assert "latin" in result
    assert "latin-ext" in result
    assert "font-thai" in result["thai"]
    assert "font-latin.woff" in result["latin"]
    assert "font-latin-ext" in result["latin-ext"]


def test_parse_css_subsets_no_comments():
    css = "@font-face { src: url(https://example.com/font.woff); }"
    result = _parse_css_subsets(css)
    assert result == {"": css}


def test_get_fonturl_subset_found_without_matching_format_raises(monkeypatch):
    css = (
        "/* thai */\n"
        "@font-face { src: url(https://example.com/font-thai.ttf); }\n"
        "/* latin */\n"
        "@font-face { src: url(https://example.com/font-latin.woff2); }\n"
    )

    class DummyResponse:
        text = css

        def raise_for_status(self):
            return None

    monkeypatch.setattr("pyfonts.utils.requests.get", lambda _: DummyResponse())

    with pytest.raises(RuntimeError, match="No font files found in formats"):
        _get_fonturl(
            endpoint="https://example.com/css",
            family="Example",
            weight=400,
            italic=False,
            allowed_formats=["woff2"],
            use_cache=False,
            subset="thai",
        )


def test_get_fonturl_subset_missing_falls_back_to_full_css(monkeypatch):
    css = "/* latin */\n" "@font-face { src: url(https://example.com/font-latin.woff2); }\n"

    class DummyResponse:
        text = css

        def raise_for_status(self):
            return None

    monkeypatch.setattr("pyfonts.utils.requests.get", lambda _: DummyResponse())

    url = _get_fonturl(
        endpoint="https://example.com/css",
        family="Example",
        weight=400,
        italic=False,
        allowed_formats=["woff2"],
        use_cache=False,
        subset="thai",
    )

    assert url == "https://example.com/font-latin.woff2"


def test_get_fonturl_subset_lookup_is_case_insensitive(monkeypatch):
    css = "/* latin */\n" "@font-face { src: url(https://example.com/font-latin.woff2); }\n"

    class DummyResponse:
        text = css

        def raise_for_status(self):
            return None

    monkeypatch.setattr("pyfonts.utils.requests.get", lambda _: DummyResponse())

    url = _get_fonturl(
        endpoint="https://example.com/css",
        family="Example",
        weight=400,
        italic=False,
        allowed_formats=["woff2"],
        use_cache=False,
        subset=" LATIN ",
    )

    assert url == "https://example.com/font-latin.woff2"


def test_map_weight_to_numeric():
    assert _map_weight_to_numeric("thin") == 100
    assert _map_weight_to_numeric("extra-light") == 200
    assert _map_weight_to_numeric("light") == 300
    assert _map_weight_to_numeric("regular") == 400
    assert _map_weight_to_numeric("medium") == 500
    assert _map_weight_to_numeric("semi-bold") == 600
    assert _map_weight_to_numeric("bold") == 700
    assert _map_weight_to_numeric("extra-bold") == 800
    assert _map_weight_to_numeric("black") == 900

    assert _map_weight_to_numeric(200) == 200
    assert _map_weight_to_numeric(700) == 700

    with pytest.raises(ValueError, match="Invalid weight descriptor: "):
        _map_weight_to_numeric("invalid-weight")
