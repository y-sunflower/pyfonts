from pyfonts import set_default, load_google_font
import matplotlib.pyplot as plt


def test_set_default():
    # check that the default font is set correctly
    set_default(load_google_font("Barrio"))
    assert plt.rcParams["font.family"] == ["Barrio"]

    # and that one can re-override
    set_default(load_google_font("Lato", weight="thin"))
    assert plt.rcParams["font.family"] == ["Lato Hairline"]
