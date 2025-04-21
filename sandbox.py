import matplotlib.pyplot as plt
from pyfonts import load_google_font

font = load_google_font("Roboto", italic=True)  # default Roboto font

fig, ax = plt.subplots()
ax.text(x=0.2, y=0.3, s="Hey there!", size=30, font=font)
