# Set default font

::: pyfonts.set_default_font

<br>

## Example

```py hl_lines="4 5"
# mkdocs: render
from pyfonts import set_default_font, load_google_font

font = load_google_font("Bitcount")
set_default_font(font) # Sets font for all text

fig, ax = plt.subplots()

x = [0, 1, 2, 3]
y = [x**2 for x in x]

# x/y tick labels, legend entries, title etc.
# will all be in Bitcount
ax.plot(x, y, "-o", label='y = x²')
ax.set_title('Simple Line Chart')
ax.text(x=0, y=5, s="Using new default font", size=20)
ax.text(x=0, y=4, s="Using a specific font", size=20, font=load_google_font("Roboto"))
ax.legend()
```
