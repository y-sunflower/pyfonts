import re
from urllib.parse import parse_qs, urlparse


def _is_url(s: str) -> bool:
    """
    Tests whether a string is an url.

    Args:
       s: a string.

    Returns:
       a boolean indicating whether the string is an url or not.
    """
    parseResult = urlparse(s)
    is_an_url: bool = (
        parseResult.scheme in ["http", "https"] and parseResult.netloc != ""
    )
    return is_an_url


def _is_valid_raw_url(url: str) -> bool:
    """
    Tests whether a given URL points to a raw font file by checking:
    - If the extension is a common font format (.ttf, .otf, .woff, .woff2)
    - If it's a GitHub URL, whether it's in a valid raw format

    Args:
       url: the url of the font file.

    Returns:
       a boolean indicating whether the url likely corresponds to a raw font file.
    """
    # Check file extension
    font_pattern = r".+\.(ttf|otf|woff2?|eot)(\?.*)?$"
    if not re.match(font_pattern, url, re.IGNORECASE):
        return False

    parsed = urlparse(url)

    # Non-GitHub URLs are accepted if the extension is valid
    return (
        "github.com" not in parsed.netloc
        and "raw.githubusercontent.com" not in parsed.netloc
    ) or (
        "raw.githubusercontent.com" in parsed.netloc
        or "/raw/" in parsed.path
        or parse_qs(parsed.query).get("raw") == ["true"]
    )
