from matplotlib.figure import Figure

from pyfonts import preview_font


def test_preview_font():
    fig: Figure = preview_font(
        "https://github.com/y-sunflower/pyfonts/blob/main/tests/Ultra-Regular.ttf?raw=true"
    )

    assert isinstance(fig, Figure)
