import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(-2 * np.pi, 2 * np.pi, 170, endpoint=True)
F1 = np.sin(X**3 / 2)
ax = plt.gca()
# ax.spines['top'].set_color('none')
# ax.spines['right'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
# ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.xticks( [-6.28, -3.14, 3.14, 6.28],
        [r'$-2\pi$', r'$-\pi$', r'$+\pi$', r'$+2\pi$'])
plt.yticks([-3, -1, 0, +1, 3])
for xtick in ax.get_xticklabels():
    xtick.set_fontsize(18)
    xtick.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7 ))
for ytick in ax.get_yticklabels():
    ytick.set_fontsize(14)
    ytick.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7 ))
    
figures = plt.plot(X, F1, label="$sin(x)$")
print(figures)
# line.zorder=1.6 # without this line it should work but doesn't
plt.legend(loc='lower left')
# ax.set_axisbelow('line')

plt.show()
# plt.savefig('axisbelow-line.png')
# ax.set_axisbelow(True)
# plt.savefig('axisbelow-true.png')
# ax.set_axisbelow(False)
# plt.savefig('axisbelow-false.png')