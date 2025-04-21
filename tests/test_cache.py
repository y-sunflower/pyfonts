from pyfonts import load_font, clear_pyfonts_cache
import time
import pytest
import platform


def test_print_message_is_valid(capsys):
    load_font(
        "https://github.com/JosephBARBIERDARNAL/pyfonts/blob/main/tests/Ultra-Regular.ttf?raw=true"
    )

    clear_pyfonts_cache()
    captured = capsys.readouterr()

    assert captured.out.strip().startswith("Font cache cleaned: ")

    # clean twice the cache leads to a different message
    clear_pyfonts_cache()
    captured = capsys.readouterr()
    assert captured.out.strip() == "No font cache directory found. Nothing to clean."


@pytest.mark.skipif(
    platform.system() == "Windows", reason="This test does not run on Windows."
)
def test_cache_time():
    clear_pyfonts_cache()

    start = time.time()

    for _ in range(10):
        font = load_font(
            "https://github.com/JosephBARBIERDARNAL/pyfonts/blob/main/tests/Ultra-Regular.ttf?raw=true"
        )
        del font

    end = time.time()
    duration_with_cache = end - start

    clear_pyfonts_cache()

    start = time.time()

    for _ in range(10):
        font = load_font(
            "https://github.com/JosephBARBIERDARNAL/pyfonts/blob/main/tests/Ultra-Regular.ttf?raw=true",
            use_cache=False,
        )
        del font

    end = time.time()
    duration_without_cache = end - start

    assert duration_with_cache < duration_without_cache, (
        "Using the cache is less than 3 time faster: "
        f"{duration_with_cache:.2f} sec (with cache) "
        f"{duration_without_cache:.2f} sec (without cache)."
    )
