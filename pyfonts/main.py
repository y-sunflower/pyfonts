from typing import Optional
import os
import warnings

from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from matplotlib.font_manager import FontProperties

from .is_valid import _is_url, _is_valid_raw_url
from .cache import _create_cache_from_fontfile


def load_font(
    font_url: Optional[str] = None,
    use_cache: bool = True,
    font_path: Optional[str] = None,
) -> FontProperties:
    """
    Loads a FontProperties object from a remote Github repo or a local file.

    Parameters:

    - font_url: It may be one of the following:
        - A URL pointing to a binary font file from Github.
        - The local file path of the font.
    - use_cache: Whether or not to cache fonts.
    - font_path: (deprecated) The local file path of the font. Use font_url instead.

    Returns:

    - matplotlib.font_manager.FontProperties: A FontProperties object containing the loaded font.

    Raises:
    - ValueError: If both font_url and font_path are None or if the URL is invalid
    - FileNotFoundError: If the local font file cannot be found
    - Exception: For various URL or font loading errors
    """
    if font_path is not None:
        warnings.warn(
            "`font_path` argument is deprecated and will be removed in a future version."
            f" Please replace `load_font(font_path='{font_path}')` by `load_font('{font_path}')`."
        )
        font_prop = FontProperties(fname=font_path)
        try:
            font_prop.get_name()
        except FileNotFoundError:
            raise FileNotFoundError(f"Font file not found: '{font_path}'.")
        return font_prop

    if font_url is not None:
        if not _is_url(font_url):
            # if it's not an url, it should be a path
            font_prop = FontProperties(fname=font_url)
            try:
                font_prop.get_name()
            except FileNotFoundError:
                raise FileNotFoundError(f"Font file not found: '{font_url}'.")
            return font_prop
        if not _is_valid_raw_url(font_url):
            raise ValueError(
                f"""
                The URL provided ({font_url}) does not appear to be valid.
                It must point to a binary font file from Github.
                Have you forgotten to append `?raw=true` to the end of the URL?
                """
            )

        cached_fontfile, cache_dir = _create_cache_from_fontfile(font_url=font_url)
        if use_cache:
            # check if file is in cache
            if os.path.exists(cached_fontfile):
                try:
                    font_prop = FontProperties(fname=cached_fontfile)
                    font_prop.get_name()  # triggers error if invalid
                    return font_prop
                except Exception:
                    # cached file is invalid, remove and proceed to download
                    os.remove(cached_fontfile)

        try:
            response = urlopen(font_url)
            content = response.read()

            with open(cached_fontfile, "wb") as f:
                f.write(content)

            return FontProperties(fname=cached_fontfile)
        except HTTPError as e:
            if e.code == 404:
                raise Exception(
                    "404 error. The url passed does not exist: font file not found."
                )
            else:
                raise ValueError(f"An HTTPError has occurred. Code: {e.code}")
        except URLError:
            raise Exception(
                "Failed to load font. This may be due to a lack of internet connection"
                " or an environment where local files are not accessible (Pyodide, etc)."
            )
    else:
        raise ValueError("You must provide a `font_url`.")
