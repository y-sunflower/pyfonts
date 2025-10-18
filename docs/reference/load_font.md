```python
# mkdocs: render
# mkdocs: hidecode
import matplotlib
matplotlib.rcParams.update(matplotlib.rcParamsDefault)
```

# Load font

<br>

::: pyfonts.load_font

<br>

## Examples

Most font files are stored on Github, but to pass a valid font url, you need to add `?raw=true` to the end of it.

So the url goes from:

```
https://github.com/google/fonts/blob/main/ofl/amaranth/Amaranth-Bold.ttf
```

To:

```
https://github.com/google/fonts/blob/main/ofl/amaranth/Amaranth-Bold.ttf?raw=true
```

What's more, if you find a font on the Google font repo (for example, here: `https://github.com/google/fonts/`), it will probably be easier to use the [`load_google_font()`](load_google_font.md) function.

#### Basic usage

```python
# mkdocs: render
import matplotlib.pyplot as plt
from pyfonts import load_font

font = load_font(
   "https://github.com/y-sunflower/pyfonts/blob/main/tests/Ultra-Regular.ttf?raw=true"
)

fig, ax = plt.subplots()
ax.text(
   x=0.2,
   y=0.3,
   s="Hey there!",
   size=30,
   font=font
)
```

#### Custom font

```python
# mkdocs: render
import matplotlib.pyplot as plt
from pyfonts import load_font

font = load_font(
   "https://github.com/google/fonts/blob/main/ofl/amaranth/Amaranth-Bold.ttf?raw=true"
)

fig, ax = plt.subplots()
ax.text(
   x=0.2,
   y=0.3,
   s="Hey there!",
   size=30,
   font=font
)
```

#### Use multiple fonts

```python
# mkdocs: render
import matplotlib.pyplot as plt
from pyfonts import load_font

font_1 = load_font(
   "https://github.com/y-sunflower/pyfonts/blob/main/tests/Ultra-Regular.ttf?raw=true"
)
font_2 = load_font(
   "https://github.com/google/fonts/blob/main/ofl/amaranth/Amaranth-Bold.ttf?raw=true"
)

fig, ax = plt.subplots()

ax.text(
   x=0.2,
   y=0.3,
   s="Hey there!",
   size=30,
   font=font_1
)

ax.text(
   x=0.4,
   y=0.6,
   s="Hello world",
   size=30,
   font=font_2
)
```
