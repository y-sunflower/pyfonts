from typing import Literal

from pyfonts.bunny import load_bunny_font
from pyfonts.cache import clear_pyfonts_cache
from pyfonts.google import load_google_font
from pyfonts.main import load_font, set_default_font
from pyfonts.preview_font import preview_font

__version__: Literal["1.4.2"] = "1.4.2"
__all__: list[str] = [
    "clear_pyfonts_cache",
    "load_bunny_font",
    "load_font",
    "load_google_font",
    "preview_font",
    "set_default_font",
]
