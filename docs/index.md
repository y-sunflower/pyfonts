# pyfonts

<img src="https://github.com/JosephBARBIERDARNAL/static/blob/main/python-libs/pyfonts/image.png?raw=true" alt="pyfonts logo" align="right" width="150px"/>

A **simple** and **reproducible** way of using fonts in matplotlib.

![PyPI - Downloads](https://img.shields.io/pypi/dm/pyfonts)

<br>

## Quick start

```py
# mkdocs: render
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

[**See more examples**](./reference/load_google_font#examples)

## Installation

=== "stable"

    ```bash
    pip install pyfonts
    ```

=== "dev"

    ```bash
    pip install git+https://github.com/JosephBARBIERDARNAL/pyfonts.git
    ```

<br><br>
