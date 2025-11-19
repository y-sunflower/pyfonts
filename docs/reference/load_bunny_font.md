```python
# mkdocs: render
# mkdocs: hidecode
import matplotlib
matplotlib.rcParams.update(matplotlib.rcParamsDefault)
```

# Load Bunny font

<br>

::: pyfonts.load_bunny_font

<br>

## Examples

#### Basic usage

```python hl_lines="5 13"
# mkdocs: render
import matplotlib.pyplot as plt
from pyfonts import load_bunny_font

font = load_bunny_font("Alumni Sans") # default Alice font

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
from pyfonts import load_bunny_font

font = load_bunny_font("Alumni Sans", weight="bold", italic=True) # italic and bold

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
from pyfonts import load_bunny_font

font_bold = load_bunny_font("Alumni Sans", weight="bold")
font_italic = load_bunny_font("Alumni Sans", italic=True)

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

All fonts from [Bunny font](https://fonts.bunny.net/) can be used:

```python hl_lines="5 13"
# mkdocs: render
import matplotlib.pyplot as plt
from pyfonts import load_bunny_font

font = load_bunny_font("Barrio")

fig, ax = plt.subplots()
ax.text(
   x=0.1,
   y=0.3,
   s="What a weird font!",
   size=30,
   font=font
)
```
