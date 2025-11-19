from pyfonts.main import load_font
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


def preview_font(
    font_url: str,
) -> Figure:
    """
    Preview a font. `font_url` is passed to [`load_font()`](load_font.md)
    """
    font = load_font(font_url)

    fig = plt.figure(figsize=(10, 5))
    plt.text(
        0.5,
        0.5,
        "Hello, World From PyFonts!",
        fontsize=30,
        ha="center",
        va="center",
        font=font,
    )
    plt.text(
        0.5,
        0.35,
        "This is a test.",
        fontsize=25,
        ha="center",
        va="center",
        font=font,
    )
    plt.text(
        0.5,
        0.65,
        "How about this?",
        fontsize=20,
        ha="center",
        va="center",
        font=font,
    )

    plt.axis("off")

    return fig
