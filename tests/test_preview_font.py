import matplotlib.pyplot as plt

from pyfonts import preview_font

import pytest


@pytest.mark.parametrize(
    "font_url",
    [
        "https://github.com/y-sunflower/pyfonts/blob/main/tests/Ultra-Regular.ttf?raw=true",
        "tests/Ultra-Regular.ttf",
    ],
)
def test_preview_font_runs_without_error(font_url):
    try:
        preview_font(font_url)
    finally:
        plt.close("all")  # Clean up to avoid any matplotlib state issues
