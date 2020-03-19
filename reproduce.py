import numpy as np
from matplotlib.ticker import FormatStrFormatter
import matplotlib.pyplot as plt


labels = np.array(['E', '', 'N', '', 'W', '', 'S', ''])
dataLength = 8
data = np.array([3.23, 3.23, 9.68, 3.23, 12.90, 32.26, 6.45, 29.03])
angles = np.linspace(0, 2*np.pi, dataLength, endpoint=False)

width = np.pi/8*np.array([1]*8)

ax = plt.subplot(111, projection='polar')
ax2 = ax.twintheta()

bars = ax.bar(angles, data, alpha=0.4, label=labels, width=width, bottom=0.0, color="red")

data = np.array([10.3, 2.23, 15.68, 13.23, 12.90, 12.26, 8.45, 29.03])
data = np.concatenate((data, [data[0]]))
angles = np.concatenate((angles, [angles[0]]))

plots = ax.plot(angles, data, alpha=0.7, linestyle="--", linewidth=1, color="blue")
plt.fill(angles, data, facecolor='blue', alpha=0.25)

gridLines, gridLabel = ax.set_thetagrids(angles * 180/np.pi, labels, fontproperties="DejaVu Sans")

plt.yticks(fontsize=8)
plt.xticks(fontsize=15)

[label.set_fontweight('bold') for label in ax.get_xticklabels()]
[label.set_color('blue') for label in ax.get_yticklabels()]
[label.set_color('red') for label in ax2.get_yticklabels()]

plt.show()