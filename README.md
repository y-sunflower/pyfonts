# pyfonts

<img src="https://github.com/JosephBARBIERDARNAL/static/blob/main/python-libs/pyfonts/image.png?raw=true" alt="Pyfonts logo" align="right" width="150px"/>

A **simple** and **reproducible** way of using fonts in matplotlib.

[![PyPI Downloads](https://static.pepy.tech/badge/pyfonts/month)](https://pepy.tech/projects/pyfonts)
![Coverage](coverage-badge.svg)

<br>

## Quick start

```py
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

[**See more examples**](https://y-sunflower.github.io/pyfonts/reference/load_google_font#examples)

<br>

## Installation

```bash
pip install pyfonts
```

<br><br>
