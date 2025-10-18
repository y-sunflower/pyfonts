import re
import os
from typing import Optional, Union, List
import requests
from matplotlib.font_manager import FontProperties

from pyfonts import load_font
from pyfonts.cache import (
    _cache_key,
    _load_cache_from_disk,
    _save_cache_to_disk,
    _MEMORY_CACHE,
    _CACHE_FILE,
)


def _map_weight_to_numeric(weight_str: Union[str, int, float]) -> int:
    weight_mapping: dict = {
        "thin": 100,
        "extra-light": 200,
        "light": 300,
        "regular": 400,
        "medium": 500,
        "semi-bold": 600,
        "bold": 700,
        "extra-bold": 800,
        "black": 900,
    }
    if isinstance(weight_str, int) or isinstance(weight_str, float):
        return int(weight_str)

    weight_str: str = weight_str.lower()
    if weight_str in weight_mapping:
        return weight_mapping[weight_str]

    raise ValueError(
        f"Invalid weight descriptor: {weight_str}. Valid options are: "
        "thin, extra-light, light, regular, medium, semi-bold, bold, extra-bold, black."
    )


def _get_fonturl_from_google(
    family: str,
    weight: Optional[Union[int, str]],
    italic: Optional[bool],
    allowed_formats: list,
    use_cache: bool,
):
    """
    Construct the Google Fonts URL for a given font family and style parameters,
    fetch the associated CSS, and extract the URL of the font file.

    Args:
        family: Name of the font family (e.g., "Roboto").
        italic: Whether the font should be italic. If None, no italic axis is set.
        weight: Numeric font weight (e.g., 400, 700). If None, no weight axis is set.
        allowed_formats: List of acceptable font file extensions (e.g., ["woff2", "ttf"]).

    Returns:
        Direct URL to the font file matching the requested style and format.
    """
    if isinstance(weight, str):
        weight: int = _map_weight_to_numeric(weight)

    cache_key: str = _cache_key(family, weight, italic, allowed_formats)
    if use_cache:
        if not _MEMORY_CACHE and os.path.exists(_CACHE_FILE):
            _MEMORY_CACHE.update(_load_cache_from_disk())
        if cache_key in _MEMORY_CACHE:
            return _MEMORY_CACHE[cache_key]

    url: str = f"https://fonts.googleapis.com/css2?family={family.replace(' ', '+')}"
    settings: dict = {}

    if italic is not None:
        settings["ital"] = str(int(italic))
    if weight is not None:
        if not (100 <= weight <= 900):
            raise ValueError(f"`weight` must be between 100 and 900, not {weight}.")
        settings["wght"] = str(int(weight))
    if settings:
        axes = ",".join(settings.keys())
        values = ",".join(settings.values())
        url += f":{axes}@{values}"

    response = requests.get(url)
    response.raise_for_status()
    css_text = response.text

    formats_pattern = "|".join(map(re.escape, allowed_formats))
    font_urls: list = re.findall(
        rf"url\((https://[^)]+\.({formats_pattern}))\)", css_text
    )
    if not font_urls:
        raise RuntimeError(
            f"No font files found in formats {allowed_formats} for '{family}'"
        )

    for fmt in allowed_formats:
        for font_url, ext in font_urls:
            if ext == fmt:
                if use_cache:
                    _MEMORY_CACHE[cache_key] = font_url
                    _save_cache_to_disk()
                return font_url


def load_google_font(
    family: str,
    weight: Optional[Union[int, str]] = None,
    italic: Optional[bool] = None,
    allowed_formats: List[str] = ["woff2", "woff", "ttf", "otf"],
    use_cache: bool = True,
    danger_not_verify_ssl: bool = False,
) -> FontProperties:
    """
    Load a font from Google Fonts with specified styling options and return a font property
    object that you can then use in your matplotlib charts.

    The easiest way to find the font you want is to browse [Google font](https://fonts.google.com/)
    and then pass the font name to the `family` argument.

    Args:
        family: Font family name (e.g., "Open Sans", "Roboto", etc).
        weight: Desired font weight (e.g., 400, 700) or one of: 'thin', 'extra-light', 'light',
        'regular', 'medium', 'semi-bold', 'bold', 'extra-bold', 'black'. Default is None.
        italic: Whether to use the italic variant. Default is None.
        allowed_formats: List of acceptable font file formats. Defaults to ["woff2", "woff", "ttf", "otf"].
        use_cache: Whether or not to cache fonts (to make pyfonts faster). Default to `True`.
        danger_not_verify_ssl: Whether or not to to skip SSL certificate on
        `ssl.SSLCertVerificationError`. If `True`, it's a **security risk** (such as data breaches or
        man-in-the-middle attacks), but can be convenient in some cases, like local
        development when behind a firewall.

    Returns:
        matplotlib.font_manager.FontProperties: A `FontProperties` object containing the loaded font.

    Examples:

        ```python
        from pyfonts import load_google_font

        font = load_google_font("Roboto") # default Roboto font
        font = load_google_font("Roboto", weight="bold") # bold font
        font = load_google_font("Roboto", italic=True) # italic font
        font = load_google_font("Roboto", weight="bold", italic=True) # italic and bold
        ```
    """
    font_url = _get_fonturl_from_google(
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
