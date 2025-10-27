<div align="center" style="font-size: 1.6em">

# pyfonts

[![PyPI Downloads](https://static.pepy.tech/badge/pyfonts)](https://pepy.tech/projects/pyfonts)
![Coverage](coverage-badge.svg)

<img src="https://github.com/JosephBARBIERDARNAL/static/blob/main/python-libs/pyfonts/image.png?raw=true" alt="Pyfonts logo" align="right" width="150px"/>

</div>

A **simple** and **reproducible** way of using fonts in matplotlib. In short, `pyfonts`:

- allows you to use all **Google Font** fonts
- allows you to use any font from an **arbitrary URL**
- is **fast** (thanks to its cache system)

<br>

## Quick start

```python
import matplotlib.pyplot as plt
from pyfonts import load_google_font

font = load_google_font("Fascinate Inline")

fig, ax = plt.subplots()
ax.text(
    x=0.2,
    y=0.5,
    s="Hey there!",
    size=30,
    font=font
)
```

![](https://raw.githubusercontent.com/y-sunflower/pyfonts/refs/heads/main/quickstart.png)

[**See more examples**](https://y-sunflower.github.io/pyfonts/#quick-start)

<br>

## Installation

```bash
pip install pyfonts
```
