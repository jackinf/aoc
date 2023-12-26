import numpy as np
import matplotlib.pyplot as plt


x0, y0 = 0, 0
dx, dy = 2, 3

x1, y1 = x0 + dx, y0 + dy

fig, ax = plt.subplots()

plt.plot([x0, x1], [y0, y1], marker='o')

plt.show()