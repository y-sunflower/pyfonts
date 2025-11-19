import os
from fontTools.ttLib import woff2


def _decompress_woff_to_ttf(font_url: str) -> str:
    output_path: str = os.path.splitext(font_url)[0] + ".ttf"
    woff2.decompress(font_url, output_path)
    return output_path
