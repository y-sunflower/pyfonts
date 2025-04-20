import pytest
from matplotlib.font_manager import FontProperties
from pyfonts import load_google_font
from pyfonts.google import _map_weight_to_numeric, _get_fonturl_from_google
from pyfonts.is_valid import _is_url, _is_valid_raw_url


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

    with pytest.raises(ValueError):
        _map_weight_to_numeric("invalid-weight")


@pytest.mark.parametrize("family", ["Roboto", "Open Sans"])
@pytest.mark.parametrize("weight", [300, 500, 800])
@pytest.mark.parametrize("italic", [True, False])
def test_get_fonturl_from_google(family, weight, italic):
    url = _get_fonturl_from_google(
        family,
        weight=weight,
        italic=italic,
        allowed_formats=["woff2", "woff", "ttf", "otf"],
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
