import pytest
import json
from pyfonts import clear_pyfonts_cache, load_font, load_google_font
from pyfonts.cache import _load_cache_from_disk
import sys

pytestmark = pytest.mark.skipif(
    sys.platform.startswith("win"),
    reason="Windows is just too weird",
)


def test_load_cache_when_file_missing(tmp_path, monkeypatch):
    monkeypatch.setattr("pyfonts.cache._CACHE_FILE", tmp_path / "missing.json")
    assert _load_cache_from_disk() == {}


def test_load_cache_valid_file(tmp_path, monkeypatch):
    data = {"a": 1}
    fp = tmp_path / "cache.json"
    fp.write_text(json.dumps(data))
    monkeypatch.setattr("pyfonts.cache._CACHE_FILE", fp)
    assert _load_cache_from_disk() == data


def test_load_cache_invalid_json(tmp_path, monkeypatch):
    fp = tmp_path / "cache.json"
    fp.write_text("{invalid json")
    monkeypatch.setattr("pyfonts.cache._CACHE_FILE", fp)
    assert _load_cache_from_disk() == {}


@pytest.mark.parametrize("use_cache", [True, False])
@pytest.mark.parametrize("verbose", [True, False])
def test_pyfonts_cache(verbose, use_cache, capsys):
    clear_pyfonts_cache(verbose=False)

    _ = load_font(
        "https://github.com/y-sunflower/pyfonts/blob/main/tests/Ultra-Regular.ttf?raw=true",
        use_cache=use_cache,
    )
    _ = load_google_font("Roboto", use_cache=use_cache)

    clear_pyfonts_cache(verbose=verbose)

    captured = capsys.readouterr()

    if verbose:
        all(s in captured.out for s in ["Google Fonts", "Font cache cleaned"])
    else:
        assert captured.out == ""

    clear_pyfonts_cache(verbose=True)
    captured = capsys.readouterr()
    if verbose:
        assert "No font cache directory found" in captured.out
