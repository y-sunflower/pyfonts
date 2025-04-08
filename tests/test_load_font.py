import pytest
from matplotlib.font_manager import FontProperties
from pyfonts import load_font


@pytest.mark.parametrize(
    "font_url",
    [
        "https://github.com/JosephBARBIERDARNAL/pyfonts/blob/main/tests/Ultra-Regular.ttf?raw=true",
        "tests/Ultra-Regular.ttf",
    ],
)
@pytest.mark.parametrize(
    "use_cache",
    [
        True,
        False,
    ],
)
def test_load_font(font_url, use_cache):
    font = load_font(font_url, use_cache=use_cache)
    assert isinstance(font, FontProperties)
    assert font.get_family() == ["sans-serif"]
    assert font.get_name() == "Ultra"
    assert font.get_style() == "normal"


def test_load_font_invalid_input():
    font_url = "/path/to/font.ttf"
    with pytest.raises(FileNotFoundError, match=f"Font file not found: '{font_url}'."):
        load_font(font_url)


def test_load_font_warning():
    font_path = "tests/Ultra-Regular.ttf"
    match = (
        "`font_path` argument is deprecated and will be removed in a future version."
    )
    f" Please replace `load_font(font_path='{font_path}')` by `load_font('{font_path}')`."
    with pytest.warns(UserWarning, match=match):
        load_font(font_path=font_path)


def test_load_font_no_input():
    with pytest.raises(ValueError, match="You must provide a `font_url`."):
        load_font()
