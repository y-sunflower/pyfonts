import requests
import re


def _get_all_fonturls_from_google(family, allowed_formats):
    url = f"https://fonts.googleapis.com/css2?family={family.replace(' ', '+')}&capability=VF"
    response = requests.get(url)
    response.raise_for_status()
    css_text = response.text

    formats_pattern = "|".join(map(re.escape, allowed_formats))
    font_urls = re.findall(rf"url\((https://[^)]+\.({formats_pattern}))\)", css_text)

    if not font_urls:
        raise RuntimeError(
            f"No font files found in formats {allowed_formats} for family '{family}'"
        )

    return [url for url, _ in font_urls]


print(
    _get_all_fonturls_from_google(
        "Roboto", allowed_formats=["woff2", "woff", "ttf", "otf"]
    )
)
print(
    _get_all_fonturls_from_google(
        "Asimovian", allowed_formats=["woff2", "woff", "ttf", "otf"]
    )
)
