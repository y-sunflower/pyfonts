from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from matplotlib.font_manager import FontProperties
from urllib.parse import urlparse
from typing import Optional
import os
import shutil
import hashlib
import warnings
import tempfile

from .is_valid import _is_url, _is_valid_raw_url


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

        if use_cache:
            cached_fontfile, cache_dir = _create_cache_from_fontfile(font_url=font_url)

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
            fd, fname = tempfile.mkstemp()
            with open(fname, "wb") as ff:
                ff.write(response.read())

            font_prop = FontProperties(fname=fname)
            font_prop.get_name()
            os.close(fd)
            os.remove(fname)
            return font_prop

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
        # finally:
        #     if os.path.exists(fname):
        #         os.remove(fname)
    else:
        raise ValueError("You must provide a `font_url`.")


def clear_pyfonts_cache() -> None:
    """
    Cleans the entire font cache directory by deleting all cached font files.
    """
    cache_dir = _get_cache_dir()
    if os.path.exists(cache_dir):
        shutil.rmtree(cache_dir)
        print(f"Font cache cleaned: {cache_dir}")
    else:
        print("No font cache directory found. Nothing to clean.")


def _create_cache_from_fontfile(font_url):
    parsed_url = urlparse(font_url)
    url_path = parsed_url.path
    filename = os.path.basename(url_path)
    _, ext = os.path.splitext(filename)
    url_hash = hashlib.sha256(font_url.encode()).hexdigest()
    cache_filename = f"{url_hash}{ext}"
    cache_dir = os.path.join(os.path.expanduser("~"), ".cache", "pyfontsloader")
    os.makedirs(cache_dir, exist_ok=True)
    cached_fontfile = os.path.join(cache_dir, cache_filename)
    return cached_fontfile, cache_dir


def _get_cache_dir() -> str:
    return os.path.join(os.path.expanduser("~"), ".cache", "pyfontsloader")
