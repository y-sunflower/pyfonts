> PyFonts is supported by [Matplotlib Journey](https://www.matplotlib-journey.com/), an interactive online course designed to make you a master of Matplotlib. If you want to **support PyFonts** and **become a Matplotlib expert**, consider purchasing the course!

<br><br>

# PyFonts

<img src="https://github.com/JosephBARBIERDARNAL/static/blob/main/python-libs/pyfonts/image.png?raw=true" alt="pyfonts logo" align="right" width="200px"/>

A simple (and reproducible) way to load fonts for `matplotlib`.

The aim of `pyfonts` is to do one thing, but to do it well.

Check out [the online documentation](https://python-graph-gallery.com/pyfonts/).

<br><br>

# Installation

_Note: pyfonts requires **Python 3.9** and above._

You can install `pyfonts` directly from PyPI with:

```
pip install pyfonts
```

<br><br>

# Quick start

`pyfonts` is designed to make the code of your graphs more reproducible by removing the need to add the local path to the font files. For example:

```python
from pyfonts import load_font
import matplotlib.pyplot as plt

font = load_font(
    "https://github.com/google/fonts/raw/main/apache/ultra/Ultra-Regular.ttf"
)

fig, ax = plt.subplots(figsize=(10, 6))
ax.text(
    x=0.5,
    y=0.5,
    s=f"What an easy way to load fonts, isn't it?",
    font=font,
    fontsize=20,
    ha="center",
)
plt.show()
```

![output of quick start](https://github.com/JosephBARBIERDARNAL/pyfonts/blob/main/img/quickstart.png?raw=true)

<br><br>

# Usage guide

Check out [the online documentation](https://python-graph-gallery.com/pyfonts/).

<br><br>

# Contributions

Contributions and feedback are welcome.

There's not much that needs to be implemented at the moment. If you've found a bug or want to request a new feature, open an [issue](https://github.com/JosephBARBIERDARNAL/pyfonts/issues).

<br><br><br>
