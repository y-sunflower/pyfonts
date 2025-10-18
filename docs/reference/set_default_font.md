# Set default font

::: pyfonts.set_default_font

<br>

## Example

```python hl_lines="4 5"
# mkdocs: render
from pyfonts import set_default_font, load_google_font

font = load_google_font("Bitcount")
set_default_font(font) # Sets font for all text

fig, ax = plt.subplots()

ax.plot([0, 1, 2, 3, 4], label='hello')
ax.set_title('Simple Line Chart')
ax.text(x=0, y=3.5, s="Using new default font", size=20)
ax.legend()

font = load_google_font("Roboto")
ax.text(x=0, y=2.5, s="Using a specific font", size=20, font=font)
```
