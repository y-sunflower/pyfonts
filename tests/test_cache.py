import os
import pytest
from pyfonts import load_font, clear_pyfonts_cache


def test_print_message_is_valid(capsys):
    load_font(
        "https://github.com/JosephBARBIERDARNAL/pyfonts/blob/main/tests/Ultra-Regular.ttf?raw=true"
    )

    clear_pyfonts_cache()
    captured = capsys.readouterr()

    if not os.name == "nt":
        assert captured.out.strip().startswith("Font cache cleaned: ")

        # clean twice the cache leads to a different message
        clear_pyfonts_cache()
        captured = capsys.readouterr()
        assert (
            captured.out.strip() == "No font cache directory found. Nothing to clean."
        )

    else:
        with pytest.raises(OSError):
            clear_pyfonts_cache()
