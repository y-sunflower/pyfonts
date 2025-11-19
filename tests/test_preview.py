from pyfonts import preview_font
from matplotlib.figure import Figure


def test_preview_font():
    fig: Figure = preview_font(
        "https://github.com/y-sunflower/pyfonts/blob/main/tests/Ultra-Regular.ttf?raw=true"
    )

    assert isinstance(fig, Figure)
