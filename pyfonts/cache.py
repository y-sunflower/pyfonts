import shutil
import hashlib
import os
from urllib.parse import urlparse


def clear_pyfonts_cache(verbose: bool = True) -> None:
    """
    Cleans the entire font cache directory by deleting all cached font files.
    """
    cache_dir = _get_cache_dir()
    if os.path.exists(cache_dir):
        shutil.rmtree(cache_dir)
        if verbose:
            print(f"Font cache cleaned: {cache_dir}")
    else:
        if verbose:
            print("No font cache directory found. Nothing to clean.")


def _create_cache_from_fontfile(font_url):
    parsed_url = urlparse(font_url)
    url_path = parsed_url.path
    filename = os.path.basename(url_path)
    _, ext = os.path.splitext(filename)
    url_hash = hashlib.sha256(font_url.encode()).hexdigest()
    cache_filename = f"{url_hash}{ext}"
    cache_dir = _get_cache_dir()
    os.makedirs(cache_dir, exist_ok=True)
    cached_fontfile = os.path.join(cache_dir, cache_filename)
    return cached_fontfile, cache_dir


def _get_cache_dir() -> str:
    return os.path.join(os.path.expanduser("~"), ".cache", "pyfontsloader")
