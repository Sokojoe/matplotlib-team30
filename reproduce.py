from matplotlib.patches import Patch
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

X = np.arange(-10, 10, 1)
Y = np.arange(-10, 10, 1)
U, V = np.meshgrid(X, Y)

q = ax.quiver(X, Y, U, V)

line, = ax.plot([3,2,1], label="label2")

qk = ax.quiverkey(q, 0.9, 0.8, U=8, label='titletitletitle', labelpos='E')

legend_elements = [
    Patch(label="title", facecolor="red"),
    qk,
    Patch(label="test3", facecolor="blue")
]

Patch(facecolor="red", edgecolor="black", label="First Element")

# ax.legend(handles=legend_elements, labels=["a", "b", "c"], loc='upper center', ncol=1)
# ax.legend(handles=legend_elements, loc='upper center', ncol=1)
# ax.legend(handles=legend_elements, loc='upper left', ncol=3)

qk2 = ax.quiverkey(q, 0.9, 0.8, U=20, label='20 unit long arrow', angle=45.0)
ax.legend(handles=[qk2, line],  loc='upper center', ncol=2, handlelength=1, borderpad=1, handletextpad=2)

# qk2 = ax.quiverkey(q, 0.9, 0.8, U=50, label='50 unit long arrow', labelpos='W')
# ax.legend(handles=[qk2, line], loc='upper center',  handlelength=8)

plt.show()
