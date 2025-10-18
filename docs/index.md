```python
# mkdocs: render
# mkdocs: hidecode
import matplotlib
matplotlib.rcParams.update(matplotlib.rcParamsDefault)
```

# pyfonts

<img src="https://github.com/JosephBARBIERDARNAL/static/blob/main/python-libs/pyfonts/image.png?raw=true" alt="Pyfonts logo" align="right" width="150px"/>

A **simple** and **reproducible** way of using fonts in matplotlib. In short, `pyfonts`:

- allows you to use all **Google Font** fonts
- allows you to use any font from an **arbitrary URL**
- is **fast** (thanks to its cache system)

[![PyPI Downloads](https://static.pepy.tech/badge/pyfonts)](https://pepy.tech/projects/pyfonts)

<br>

## Quick start

```python
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

[**See more examples**](./reference/load_google_font.md#examples)

## Installation

=== "stable"

    ```bash
    pip install pyfonts
    ```

=== "dev"

    ```bash
    pip install git+https://github.com/y-sunflower/pyfonts.git
    ```

<br><br>
