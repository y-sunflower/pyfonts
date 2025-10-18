# Load Google font

<br>

::: pyfonts.load_google_font

<br>

## Examples

#### Basic usage

```python hl_lines="5 13"
# mkdocs: render
import matplotlib.pyplot as plt
from pyfonts import load_google_font

font = load_google_font("Roboto") # default Roboto font

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

```python hl_lines="5 13"
# mkdocs: render
import matplotlib.pyplot as plt
from pyfonts import load_google_font

font = load_google_font("Roboto", weight="bold", italic=True) # italic and bold

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

```python hl_lines="5 6 15 23"
# mkdocs: render
import matplotlib.pyplot as plt
from pyfonts import load_google_font

font_bold = load_google_font("Roboto", weight="bold")
font_italic = load_google_font("Roboto", italic=True)

fig, ax = plt.subplots()

ax.text(
   x=0.2,
   y=0.3,
   s="Hey bold!",
   size=30,
   font=font_bold
)

ax.text(
   x=0.4,
   y=0.6,
   s="Hey italic!",
   size=30,
   font=font_italic
)
```

#### Fancy font

All fonts from [Google font](https://fonts.google.com/) can be used:

```python hl_lines="5 13"
# mkdocs: render
import matplotlib.pyplot as plt
from pyfonts import load_google_font

font = load_google_font("Barrio")

fig, ax = plt.subplots()
ax.text(
   x=0.1,
   y=0.3,
   s="What a weird font!",
   size=30,
   font=font
)
```
