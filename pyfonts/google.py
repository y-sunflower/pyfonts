import re
from typing import Optional, Union, List
import requests
from matplotlib.font_manager import FontProperties

from pyfonts import load_font


def _map_weight_to_numeric(weight_str: Union[str, int, float]) -> int:
    weight_mapping = {
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

    weight_str = weight_str.lower()
    if weight_str in weight_mapping:
        return weight_mapping[weight_str]

    raise ValueError(
        f"Invalid weight descriptor: {weight_str}. Valid options are: "
        "thin, extra-light, light, regular, medium, semi-bold, bold, extra-bold, black."
    )


def _get_fonturl_from_google(
    family,
    weight,
    italic,
    allowed_formats,
):
    """
    Construct the Google Fonts URL for a given font family and style parameters,
    fetch the associated CSS, and extract the URL of the font file.

    Args:
        family (str): Name of the font family (e.g., "Roboto").
        italic (bool or None): Whether the font should be italic. If None, no italic axis is set.
        weight (int or float or None): Numeric font weight (e.g., 400, 700). If None, no weight axis is set.
        width (ignored): Currently unused. Reserved for potential future support.
        allowed_formats (list[str]): List of acceptable font file extensions (e.g., ["woff2", "ttf"]).

    Returns:
        str: Direct URL to the font file matching the requested style and format.

    Raises:
        ValueError: If `italic` is not a boolean or `weight` is not a number.
        RuntimeError: If the stylesheet or font URL could not be retrieved or parsed.
    """

    if isinstance(weight, str):
        weight = _map_weight_to_numeric(weight)

    url = f"https://fonts.googleapis.com/css2?family={family.replace(' ', '+')}"
    settings = {}

    if italic is not None:
        settings["ital"] = str(int(italic))

    if weight is not None:
        if weight < 100 or weight > 900:
            raise ValueError(f"`weight` must be between 100 and 900, not {weight}.")
        settings["wght"] = str(int(weight))

    if settings:
        axes = ",".join(settings.keys())
        values = ",".join(settings.values())
        url += f":{axes}@{values}"

    response = requests.get(url)
    response.raise_for_status()

    try:
        response = requests.get(url)
        response.raise_for_status()
        css_text = response.text
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to download CSS: {e}")

    formats_pattern = "|".join(map(re.escape, allowed_formats))
    font_urls = re.findall(rf"url\((https://[^)]+\.({formats_pattern}))\)", css_text)

    if not font_urls:
        raise RuntimeError(
            f"No font files found in formats {allowed_formats} for family '{family}'"
        )

    for fmt in allowed_formats:
        for url, ext in font_urls:
            if ext == fmt:
                return url
    raise RuntimeError("No acceptable font file format found.")


def load_google_font(
    family: str,
    weight: Union[int, str] = None,
    italic: Optional[bool] = None,
    allowed_formats: List[str] = ["woff2", "woff", "ttf", "otf"],
    use_cache: bool = True,
) -> FontProperties:
    """
    Load a font from Google Fonts with specified styling options and return a font property
    object that you can then use in your matplotlib charts.

    The easiest way to find the font you want is to browse [Google font](https://fonts.google.com/)
    and then pass the font name to the `family` argument.

    Parameters
    ---

    - `family`: Font family name (e.g., "Open Sans", "Roboto", etc).

    - `weight`: Desired font weight (e.g., 400, 700) or one of: 'thin', 'extra-light', 'light',
        'regular', 'medium', 'semi-bold', 'bold', 'extra-bold', 'black'. Default is None.

    - `italic`: Whether to use the italic variant. Default is None.

    - `allowed_formats`: List of acceptable font file formats. Defaults to ["woff2", "woff", "ttf", "otf"].

    - `use_cache`: Whether or not to cache fonts (to make pyfonts faster). Default to `True`.

    Returns
    ---

    - `matplotlib.font_manager.FontProperties`: A `FontProperties` object containing the loaded font.

    Usage
    ---

    ```py
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
    )
    fontprop = load_font(font_url, use_cache=use_cache)
    return fontprop


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    font = load_google_font("Roboto", weight="thin", italic=False)

    fig, ax = plt.subplots()
    ax.text(x=0.1, y=0.2, s="Hello there, you good?", size=30, font=font)
    plt.show()
