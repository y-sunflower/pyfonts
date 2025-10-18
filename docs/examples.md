## Quick start

The easiest (and recommended) way of using `pyfonts` is to find the name of a font you like on [Google font](https://fonts.google.com/){target="\_blank"} and pass it to `load_google_font()`:

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
   font=font # We pass it to the `font` argument
)
```

## Bold/light fonts

In order to have a **bold** font, you can use the `weight` argument that accepts either one of: "thin", "extra-light", "light", "regular","medium", "semi-bold", "bold", "extra-bold", "black", or any number between 100 and 900 (the higher the bolder).

```python
# mkdocs: render
import matplotlib.pyplot as plt
from pyfonts import load_google_font

font_bold = load_google_font("Roboto", weight="bold")
font_regular = load_google_font("Roboto", weight="regular") # Default
font_light = load_google_font("Roboto", weight="thin")

fig, ax = plt.subplots()
text_params = dict(x=0.2,size=30,)
ax.text(
   y=0.7,
   s="Bold font",
   font=font_bold,
   **text_params
)
ax.text(
   y=0.5,
   s="Regular font",
   font=font_regular,
   **text_params
)
ax.text(
   y=0.3,
   s="Light font",
   font=font_light,
   **text_params
)
```

> Note that **not all fonts** have different weight and can be set to bold/light.

## Italic font

`load_google_font()` has an `italic` argument, that can either be `True` or `False` (default to `False`).

```python
# mkdocs: render
import matplotlib.pyplot as plt
from pyfonts import load_google_font

font = load_google_font("Roboto", italic=True)

fig, ax = plt.subplots()
ax.text(
   x=0.2,
   y=0.5,
   s="This text is in italic",
   size=30,
   font=font
)
```

> Note that **not all fonts** can be set to italic.

## Set font globally

If you also want to change the default font used for e.g. the axis labels, legend entries, titles, etc., you can use `set_default_font()`:

```python
# mkdocs: render
from pyfonts import set_default_font, load_google_font

font = load_google_font("Fascinate Inline")
set_default_font(font) # Sets font for all text

fig, ax = plt.subplots()

x = [0, 1, 2, 3]
y = [x**2 for x in x]

# x+y tick labels, legend entries, title etc.
# will all be in Fascinate Inline
ax.plot(x, y, "-o", label='y = x²')
ax.set_title('Simple Line Chart')
ax.text(x=0, y=5, s="Hello world", size=20)
ax.legend()

# change the font for a specific element as usual
ax.set_xlabel("x values", font=load_google_font("Roboto"), size=15)
```
