from pyfonts import load_font, clear_pyfonts_cache
import matplotlib.pyplot as plt


clear_pyfonts_cache()
font = load_font(
    "https://github.com/skosch/Crimson/blob/master/Desktop%20Fonts/TTF/Crimson-Roman.ttf?raw=true",
)

fig, ax = plt.subplots()

ax.text(x=0.5, y=0.5, s="hey", font=font)
