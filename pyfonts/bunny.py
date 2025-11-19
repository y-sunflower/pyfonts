from typing import Optional, Union, List
from matplotlib.font_manager import FontProperties

from pyfonts import load_font
from pyfonts.utils import _get_fonturl


def load_bunny_font(
    family: str,
    weight: Optional[Union[int, str]] = None,
    italic: Optional[bool] = None,
    allowed_formats: List[str] = ["woff", "ttf", "otf"],
    use_cache: bool = True,
    danger_not_verify_ssl: bool = False,
) -> FontProperties:
    """
    Load a font from bunny Fonts with specified styling options and return a font property
    object that you can then use in your matplotlib charts.

    The easiest way to find the font you want is to browse [bunny font](https://fonts.bunny.net/)
    and then pass the font name to the `family` argument.

    Args:
        family: Font family name (e.g., "Open Sans", "Roboto", etc).
            weight: Desired font weight (e.g., 400, 700) or one of 'thin', 'extra-light', 'light',
            'regular', 'medium', 'semi-bold', 'bold', 'extra-bold', 'black'. Default is `None`.
        italic: Whether to use the italic variant. Default is `None`.
        allowed_formats: List of acceptable font file formats. Defaults to ["woff", "ttf", "otf"].
            Note that for `woff2` fonts to work, you must have [brotli](https://github.com/google/brotli)
            installed.
        use_cache: Whether or not to cache fonts (to make pyfonts faster). Default to `True`.
        danger_not_verify_ssl: Whether or not to to skip SSL certificate on
            `ssl.SSLCertVerificationError`. If `True`, it's a **security risk** (such as data breaches or
            man-in-the-middle attacks), but can be convenient in some cases, like local
            development when behind a firewall.

    Returns:
        matplotlib.font_manager.FontProperties: A `FontProperties` object containing the loaded font.

    Examples:

        ```python
        from pyfonts import load_bunny_font

        font = load_bunny_font("Roboto") # default Roboto font
        font = load_bunny_font("Roboto", weight="bold") # bold font
        font = load_bunny_font("Roboto", italic=True) # italic font
        font = load_bunny_font("Roboto", weight="bold", italic=True) # italic and bold
        ```
    """
    font_url = _get_fonturl(
        endpoint="https://fonts.bunny.net/css",
        family=family,
        weight=weight,
        italic=italic,
        allowed_formats=allowed_formats,
        use_cache=use_cache,
    )

    return load_font(
        font_url,
        use_cache=use_cache,
        danger_not_verify_ssl=danger_not_verify_ssl,
    )
