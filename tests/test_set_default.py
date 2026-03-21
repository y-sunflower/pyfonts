from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

import pyfonts.main as pyfonts_main
from pyfonts import set_default_font
from pyfonts.utils import _attach_font_provider_metadata


TEST_FONT = Path(__file__).with_name("Amarante-Regular.ttf")
ALT_TEST_FONT = Path(__file__).with_name("Ultra-Regular.ttf")


def test_set_default_with_local_font(monkeypatch):
    added_fonts = []
    monkeypatch.setattr(pyfonts_main.fontManager, "addfont", added_fonts.append)

    with mpl.rc_context():
        font = FontProperties(fname=str(TEST_FONT))
        set_default_font(font)

        assert plt.rcParams["font.family"] == [font.get_name()]
        assert added_fonts == [str(TEST_FONT)]


def test_set_default_registers_provider_variants(monkeypatch):
    font = FontProperties(fname=str(TEST_FONT))
    _attach_font_provider_metadata(
        font,
        endpoint="https://fonts.googleapis.com/css2",
        family="Test Family",
        allowed_formats=["ttf"],
        use_cache=True,
        danger_not_verify_ssl=False,
    )

    added_fonts = []
    calls = []
    variant_fonts = {
        "https://example.com/regular.ttf": FontProperties(fname=str(TEST_FONT)),
        "https://example.com/bold-italic.ttf": FontProperties(fname=str(ALT_TEST_FONT)),
    }

    def fake_get_fonturl(endpoint, family, weight, italic, allowed_formats, use_cache):
        calls.append(
            (endpoint, family, weight, italic, tuple(allowed_formats), use_cache)
        )
        if weight == 400 and italic is False:
            return "https://example.com/regular.ttf"
        if weight == 700 and italic is True:
            return "https://example.com/bold-italic.ttf"
        raise ValueError("variant not available")

    def fake_load_font(font_url, use_cache, danger_not_verify_ssl):
        return variant_fonts[font_url]

    monkeypatch.setattr(pyfonts_main, "_get_fonturl", fake_get_fonturl)
    monkeypatch.setattr(pyfonts_main, "load_font", fake_load_font)
    monkeypatch.setattr(pyfonts_main.fontManager, "addfont", added_fonts.append)

    with mpl.rc_context():
        set_default_font(font)

        assert plt.rcParams["font.family"] == [font.get_name(), "Test Family"]
        assert set(added_fonts) == {str(TEST_FONT), str(ALT_TEST_FONT)}
        assert any(
            weight == 700 and italic is True for _, _, weight, italic, _, _ in calls
        )
