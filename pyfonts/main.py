from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from tempfile import NamedTemporaryFile
from matplotlib.font_manager import FontProperties
from urllib.parse import urlparse
from typing import Optional
import os
import shutil
import hashlib
import warnings

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
            # generate cache path
            parsed_url = urlparse(font_url)
            url_path = parsed_url.path
            filename = os.path.basename(url_path)
            _, ext = os.path.splitext(filename)
            url_hash = hashlib.sha256(font_url.encode()).hexdigest()
            cache_filename = f"{url_hash}{ext}"
            cache_dir = os.path.join(os.path.expanduser("~"), ".cache", "pyfontsloader")
            os.makedirs(cache_dir, exist_ok=True)
            cache_path = os.path.join(cache_dir, cache_filename)

            # check cache
            if os.path.exists(cache_path):
                try:
                    font_prop = FontProperties(fname=cache_path)
                    font_prop.get_name()
                    return font_prop
                except Exception:
                    # cached file is invalid, remove and proceed to download
                    os.remove(cache_path)

        try:
            response = urlopen(font_url)
            content = response.read()

            temp_file = NamedTemporaryFile(
                dir=cache_dir if use_cache else None, delete=os.name == "nt"
            )
            temp_path = temp_file.name
            try:
                with open(temp_path, "wb") as f:
                    f.write(content)
                font_prop = FontProperties(fname=temp_path)
                font_prop.get_name()
                # If cache is enabled, move to cache
                if use_cache:
                    os.replace(temp_path, cache_path)
                else:
                    return FontProperties(fname=temp_path)
            except:
                if os.path.exists(temp_path):
                    os.remove(temp_path)
                raise
            finally:
                if os.path.exists(temp_path) and use_cache and not os.name == "nt":
                    os.remove(temp_path)

            return FontProperties(fname=cache_path)
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
                " or an environment where local files are not accessible."
            )
    else:
        raise ValueError("You must provide a `font_url`.")


def clear_pyfonts_cache() -> None:
    """
    Cleans the entire font cache directory by deleting all cached font files.
    """
    cache_dir = os.path.join(os.path.expanduser("~"), ".cache", "pyfontsloader")
    if os.path.exists(cache_dir):
        shutil.rmtree(cache_dir)
        print(f"Font cache cleaned: {cache_dir}")
    else:
        print("No font cache directory found. Nothing to clean.")
