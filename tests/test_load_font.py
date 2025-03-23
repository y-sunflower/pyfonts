import pytest
from matplotlib.font_manager import FontProperties
from pyfonts import load_font


def test_load_font_with_url():
    font = load_font(
        "https://github.com/JosephBARBIERDARNAL/pyfonts/blob/main/tests/Ultra-Regular.ttf?raw=true"
    )
    assert isinstance(font, FontProperties)


def test_load_font_with_path():
    font = load_font("tests/Ultra-Regular.ttf")
    assert isinstance(font, FontProperties)


def test_load_font_invalid_input():
    with pytest.raises(FileNotFoundError):
        load_font("/path/to/font.ttf")


def test_load_font_warning():
    with pytest.warns(UserWarning):
        load_font(font_path="tests/Ultra-Regular.ttf")


def test_load_font_no_input():
    with pytest.raises(ValueError):
        load_font()
