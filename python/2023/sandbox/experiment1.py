import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


fig, ax = plt.subplots()

x = np.linspace(0, 10, 200)
y = np.sin(x)

rect = patches.Rectangle((0.1, 0.2), 0.5, 0.4, linewidth=1, edgecolor='r', facecolor='none')
ax.add_patch(rect)

ax.plot(x, y)
plt.show()