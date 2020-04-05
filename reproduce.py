from matplotlib.patches import Patch
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

X = np.arange(-10, 10, 1)
Y = np.arange(-10, 10, 1)
U, V = np.meshgrid(X, Y)

q = ax.quiver(X, Y, U, V)

qk = ax.quiverkey(q, 0.9, 0.8, U=10, label='titletitletitle', labelpos='E')

legend_elements = [
    Patch(label="test1", facecolor="red"),
    qk,
    Patch(label="test3", facecolor="blue")
]

Patch(facecolor="red", edgecolor="black", label="First Element")

ax.legend(handles=legend_elements, loc='lower right', ncol=3)
# ax.legend(handles=legend_elements, loc='upper right', ncol=1)

plt.show()