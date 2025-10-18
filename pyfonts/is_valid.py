import re
from urllib.parse import urlparse, parse_qs


def _is_url(s: str) -> bool:
    """
    Tests whether a string is an url.

    Parameters:
       - s: a string.

    Returns:
       - a boolean indicating whether the string is an url or not.
    """
    is_an_url: bool = urlparse(s).scheme != ""
    return is_an_url


def _is_valid_raw_url(url: str) -> bool:
    """
    Tests whether a given URL points to a raw font file by checking:
    - If the extension is a common font format (.ttf, .otf, .woff, .woff2)
    - If it's a GitHub URL, whether it's in a valid raw format

    Parameters:
       - url: the url of the font file.

    Returns:
       - a boolean indicating whether the url likely corresponds to a raw font file.
    """
    # Check file extension
    font_pattern = r".+\.(ttf|otf|woff2?|eot)(\?.*)?$"
    if not re.match(font_pattern, url, re.IGNORECASE):
        return False

    parsed = urlparse(url)

    # Non-GitHub URLs are accepted if the extension is valid
    if (
        "github.com" not in parsed.netloc
        and "raw.githubusercontent.com" not in parsed.netloc
    ):
        return True

    # GitHub raw subdomain
    if "raw.githubusercontent.com" in parsed.netloc:
        return True

    # Check for /raw/ in path (e.g., /user/repo/raw/branch/file)
    if "/raw/" in parsed.path:
        return True

    # Check for ?raw=true in query string, even with extra params
    query_params: dict[str, list[str]] = parse_qs(parsed.query)
    if "raw" in query_params and query_params["raw"] == ["true"]:
        return True

    return False
