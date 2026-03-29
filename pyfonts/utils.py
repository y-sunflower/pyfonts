import re
import os
from typing import Any, Optional, Union
import requests

from matplotlib.font_manager import FontProperties

from pyfonts.cache import (
    _cache_key,
    _load_cache_from_disk,
    _save_cache_to_disk,
    _MEMORY_CACHE,
    _CACHE_FILE,
)

_FONT_PROVIDER_METADATA_ATTR = "_pyfonts_provider_metadata"


def _parse_css_subsets(css_text: str) -> dict[str, str]:
    parts = re.split(r"/\*\s*(\S+)\s*\*/", css_text)
    if len(parts) < 3:
        return {"": css_text}
    subsets: dict[str, str] = {}
    for i in range(1, len(parts), 2):
        name = parts[i]
        block = parts[i + 1] if i + 1 < len(parts) else ""
        subsets[name] = block
    return subsets


def _get_fonturl(
    endpoint: str,
    family: str,
    weight: Optional[Union[int, str]],
    italic: Optional[bool],
    allowed_formats: list,
    use_cache: bool,
    subset: str = "latin",
) -> Optional[str]:
    """
    Construct the URL for a given endpoint, font family and style parameters,
    fetch the associated CSS, and extract the URL of the font file.

    Args:
        enpoint: URL of the font provider.
        family: Name of the font family (e.g., "Roboto").
        italic: Whether the font should be italic. If None, no italic axis is set.
        weight: Numeric font weight (e.g., 400, 700). If None, no weight axis is set.
        allowed_formats: List of acceptable font file extensions (e.g., ["woff2", "ttf"]).
        use_cache: Whether or not to cache fonts (to make pyfonts faster).
        subset: Unicode subset to select from the CSS (e.g., "latin", "thai"). Defaults to "latin".

    Returns:
        Direct URL to the font file matching the requested style and format.
    """
    if isinstance(weight, str):
        weight: int = _map_weight_to_numeric(weight)

    cache_key: str = _cache_key(family, weight, italic, allowed_formats, subset)
    if use_cache:
        if not _MEMORY_CACHE and os.path.exists(_CACHE_FILE):
            _MEMORY_CACHE.update(_load_cache_from_disk())
        if cache_key in _MEMORY_CACHE:
            return _MEMORY_CACHE[cache_key]

    url: str = f"{endpoint}?family={family.replace(' ', '+')}"
    settings: dict = {}

    if italic:
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

    # for some reason, Bunny fonts sends this text response instead of an
    # actual error message, so we handle it ourselves manually.
    if "Error: API Error" in css_text and "No families available" in css_text:
        raise ValueError(
            f"No font available for the request at URL: {url}. "
            "Maybe the font variant (italic, bold, etc) you're looking for"
            " does not exist."
        )

    subsets = _parse_css_subsets(css_text)
    search_text = subsets.get(subset, css_text)

    formats_pattern = "|".join(map(re.escape, allowed_formats))
    font_urls: list = re.findall(
        rf"url\((https://[^)]+\.({formats_pattern}))\)", search_text
    )

    if not font_urls:
        font_urls = re.findall(
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


def _attach_font_provider_metadata(
    font: FontProperties,
    *,
    endpoint: str,
    family: str,
    allowed_formats: list[str],
    use_cache: bool,
    danger_not_verify_ssl: bool,
) -> FontProperties:
    setattr(
        font,
        _FONT_PROVIDER_METADATA_ATTR,
        {
            "endpoint": endpoint,
            "family": family,
            "allowed_formats": list(allowed_formats),
            "use_cache": use_cache,
            "danger_not_verify_ssl": danger_not_verify_ssl,
        },
    )
    return font


def _get_font_provider_metadata(font: FontProperties) -> Optional[dict[str, Any]]:
    return getattr(font, _FONT_PROVIDER_METADATA_ATTR, None)
