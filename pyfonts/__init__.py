from .main import load_font, set_default_font
from .google import load_google_font
from .cache import clear_pyfonts_cache
from .preview_font import preview_font

from typing import Literal

__version__: Literal["1.1.1"] = "1.1.1"
__all__: list[str] = [
    "load_font",
    "load_google_font",
    "set_default_font",
    "preview_font",
    "clear_pyfonts_cache",
]
