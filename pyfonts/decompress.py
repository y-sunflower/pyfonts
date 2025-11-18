import os
from fontTools.ttLib import woff2


def _change_file_extension(file: str, to: str) -> str:
    return os.path.splitext(file)[0] + "." + to


def _decompress_woff_to_ttf(font_url: str) -> str:
    output_path: str = _change_file_extension(font_url, to="ttf")
    woff2.decompress(font_url, output_path)
    return output_path
