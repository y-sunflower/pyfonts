from pyfonts import load_google_font, set_default
import matplotlib.pyplot as plt

set_default(load_google_font("Barrio"))
plt.figure(figsize=(3, 3))
plt.plot([1, 2, 3], label="Plot")
plt.legend()

set_default(load_google_font("Lato"))
plt.title("Title")

plt.show()
