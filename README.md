<div align="center" style="font-size: 1.6em">

# pyfonts

[![PyPI Downloads](https://static.pepy.tech/badge/pyfonts)](https://pepy.tech/projects/pyfonts)
![Coverage](https://raw.githubusercontent.com/y-sunflower/pyfonts/refs/heads/main/coverage-badge.svg)
![Python Versions](https://img.shields.io/badge/Python-3.9–3.14-blue)

<img src="https://github.com/JosephBARBIERDARNAL/static/blob/main/python-libs/pyfonts/image.png?raw=true" alt="Pyfonts logo" align="right" width="150px"/>

</div>

A **simple** and **reproducible** way of using fonts in matplotlib. In short, `pyfonts`:

- allows you to use all fonts from [**Google Font**](https://fonts.google.com/)
- allows you to use all fonts from [**Bunny Font**](https://fonts.bunny.net/) (GDPR-compliant alternative to Google Fonts)
- allows you to use any font from an **arbitrary URL**
- is **efficient** (thanks to its cache system)

<br>

## Quick start

- Google Fonts

```python
import matplotlib.pyplot as plt
from pyfonts import load_google_font

font = load_google_font("Fascinate Inline")

fig, ax = plt.subplots()
ax.text(x=0.2, y=0.5, s="Hey there!", size=30, font=font)
```

![](https://raw.githubusercontent.com/y-sunflower/pyfonts/refs/heads/main/docs/img/quickstart.png)

- Bunny Fonts

```python
import matplotlib.pyplot as plt
from pyfonts import load_bunny_font

font = load_bunny_font("Barrio")

fig, ax = plt.subplots()
ax.text(x=0.2, y=0.5, s="Hey there!", size=30, font=font)
```

![](https://raw.githubusercontent.com/y-sunflower/pyfonts/refs/heads/main/docs/img/quickstart-1.png)

[**See more examples**](https://y-sunflower.github.io/pyfonts/#quick-start)

<br>

## Installation

```bash
pip install pyfonts
```
