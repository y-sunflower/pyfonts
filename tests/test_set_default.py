import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.text import Text

from pyfonts import set_default_font, load_google_font


def test_set_default():
    # check that the default font is set correctly
    set_default_font(load_google_font("Barrio"))
    assert plt.rcParams["font.family"] == ["Barrio"]

    # and that one can re-override
    set_default_font(load_google_font("Lato", weight="thin"))
    assert "Lato Hairline" in plt.rcParams["font.family"]


def test_set_default_complex():
    set_default_font(load_google_font("SN Pro"))

    fig, ax = plt.subplots()
    ax.text(x=0.2, y=0.7, s="Hey there!", size=30, style="italic", weight="bold")
    ax.text(x=0.2, y=0.5, s="Hey there!", size=30)
    ax.text(x=0.2, y=0.3, s="Hey there!", size=30, weight=900)
    ax.text(x=0.2, y=0.1, s="Hey there!", size=30, weight="bold")

    artists = ax.get_children()
    artists_text = [art for art in artists if isinstance(art, Text) and art.get_text()]
    for artist in artists_text:
        font_props = artist.get_fontproperties()
        assert font_props.get_weight() in ["bold", "normal", 900], (
            f"Unexpected weight: {font_props.get_weight()}"
        )
        assert font_props.get_style() in ["italic", "normal"]


def test_set_default_google_font_urbanist_with_matplotlib_311_hash(monkeypatch):
    def matplotlib_311_hash(self):
        # Matplotlib 3.11 hashes tuple(self.__dict__.values()). The list
        # normalization keeps this regression portable on older Matplotlib.
        values = tuple(
            tuple(value) if isinstance(value, list) else value
            for value in self.__dict__.values()
        )
        return hash(values)

    monkeypatch.setattr(FontProperties, "__hash__", matplotlib_311_hash)

    font = load_google_font("Urbanist")
    hash(font)
    set_default_font(font)

    assert plt.rcParams["font.family"][0] == "Urbanist"
