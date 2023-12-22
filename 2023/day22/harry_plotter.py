import matplotlib.pyplot as plt

with open('sample.txt', 'r') as f:
    coordinates = f.read().split('\n')

# Parsing the coordinates into a list of points
points = []
for coord in coordinates:
    start, end = coord.split('~')
    start = tuple(map(int, start.split(',')))
    end = tuple(map(int, end.split(',')))
    points.append((start, end))

# Creating a 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plotting each line segment
for start, end in points:
    ax.plot([start[0], end[0]], [start[1], end[1]], [start[2], end[2]], marker='o')

# Setting labels and title
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Visualization of Coordinates')

plt.show()
