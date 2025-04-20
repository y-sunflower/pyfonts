import re
from urllib.parse import urlparse


def _is_url(s: str) -> bool:
    """
    Tests whether a string is an url.

    Parameters:
       - s: a string.

    Returns:
       - a boolean indicating whether the string is an url or not.
    """
    is_an_url = urlparse(s).scheme != ""
    return is_an_url


def _is_valid_raw_url(url: str) -> bool:
    """
    Tests whether a given URL points to a font file by checking for common
    font file extensions, regardless of the domain.

    Parameters:
       - url: the url of the font file.

    Returns:
       - a boolean indicating whether the url likely corresponds to a raw font file.
    """
    pattern = r".+\.(ttf|otf|woff|woff2)(\?.*)?$"
    return re.match(pattern, url, re.IGNORECASE) is not None
