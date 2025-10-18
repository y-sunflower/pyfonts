import shutil
import hashlib
import os
import json
from urllib.parse import urlparse

_CACHE_FILE: str = os.path.join(
    os.path.expanduser("~"), ".cache", ".pyfonts_google_cache.json"
)
_MEMORY_CACHE: dict = {}


def _cache_key(family: str, weight, italic, allowed_formats: list[str]) -> str:
    key_str: str = json.dumps(
        {
            "family": family,
            "weight": weight,
            "italic": italic,
            "allowed_formats": allowed_formats,
        },
        sort_keys=True,
    )
    return hashlib.sha256(key_str.encode()).hexdigest()


def _load_cache_from_disk() -> dict:
    if not os.path.exists(_CACHE_FILE):
        return {}
    try:
        with open(_CACHE_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {}


def _save_cache_to_disk() -> None:
    try:
        with open(_CACHE_FILE, "w") as f:
            json.dump(_MEMORY_CACHE, f)
    except Exception:
        pass


def clear_pyfonts_cache(verbose: bool = True) -> None:
    """
    Cleans both:
      1. The font cache directory
      2. The Google Fonts URL cache

    Parameters
    ---

    - `verbose`: Whether or not to print a cache cleanup message. The default value is True.

    Usage
    ---

    ```py
    from pyfonts import clear_pyfonts_cache
    clear_pyfonts_cache()
    ```
    """
    cache_dir: str = _get_cache_dir()

    # clear the local font file cache
    if os.path.exists(cache_dir):
        shutil.rmtree(cache_dir)
        if verbose:
            print(f"Font cache cleaned: {cache_dir}")
    else:
        if verbose:
            print("No font cache directory found. Nothing to clean.")

    # clear the Google Fonts URL cache
    global _MEMORY_CACHE
    _MEMORY_CACHE.clear()

    if os.path.exists(_CACHE_FILE):
        try:
            os.remove(_CACHE_FILE)
            if verbose:
                print(f"Google Fonts URL cache cleared: {_CACHE_FILE}")
        except Exception as e:
            if verbose:
                print(f"Failed to remove Google Fonts cache file: {e}")
    else:
        if verbose:
            print("No Google Fonts cache file found. Nothing to clean.")


def _create_cache_from_fontfile(font_url):
    parsed_url = urlparse(font_url)
    url_path = parsed_url.path
    filename = os.path.basename(url_path)
    _, ext = os.path.splitext(filename)
    url_hash: str = hashlib.sha256(font_url.encode()).hexdigest()
    cache_filename: str = f"{url_hash}{ext}"
    cache_dir: str = _get_cache_dir()
    os.makedirs(cache_dir, exist_ok=True)
    cached_fontfile: str = os.path.join(cache_dir, cache_filename)
    return cached_fontfile, cache_dir


def _get_cache_dir() -> str:
    return os.path.join(os.path.expanduser("~"), ".cache", "pyfontsloader")
