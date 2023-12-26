from sympy import symbols, Eq, solve


t, u = symbols('t u')


import matplotlib.pyplot as plt
import matplotlib.patches as patches

with open('sample2.txt', 'r') as f:
    lines = f.read().split('\n')
    lines = [line.split('@') for line in lines]
    print(lines)


# Rectangle lines
A, B = 7, 27
POWER = 10
line_segments = [
    ((A, A), (A, B)),   # southern segment
    ((A, B), (B, B)),  # eastern segment
    ((A, A), (B, A)),   # western segment
    ((B, A), (B, B))  # northern segment
]

coordinates = []
for line in lines:
    coord, vec = line
    x0, y0, z0 = list(map(int, coord.strip().split(',')))
    dx, dy, dz = list(map(int, vec.strip().split(',')))
    coordinates.append((x0, y0, dx, dy))


def show_drawing():
    fig, ax = plt.subplots()

    # https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html
    width, height = B - A, B - A
    rec = patches.Rectangle((A, A), width, width, linewidth=1, edgecolor='r',facecolor='none')
    ax.add_patch(rec)

    for x0, y0, dx, dy in coordinates:
        x1 = x0 + dx * POWER
        y1 = y0 + dy * POWER

        plt.plot([x0, x1], [y0, y1], marker='o')

    fig.show()


def check_intersection(start, direction, segment):
    # Parametric equation of the ray
    ray_x = start[0] + direction[0] * t
    ray_y = start[1] + direction[1] * t

    # Parametric equation of the line segment
    segment_x = segment[0][0] + (segment[1][0] - segment[0][0]) * u
    segment_y = segment[0][1] + (segment[1][1] - segment[0][1]) * u

    # Equations to solve
    eq1 = Eq(ray_x, segment_x)
    eq2 = Eq(ray_y, segment_y)

    # Solve the system of equations
    sol = solve((eq1, eq2), (t, u))

    # Check if there is a valid intersection (t and u must be within certain ranges)
    if sol:
        t_val, u_val = sol[t], sol[u]
        if t_val >= 0 and 0 <= u_val <= 1:
            return True
    return False


show_drawing()


intersection_count = 0
for x0, y0, dx, dy in coordinates:
    for seg in line_segments:
        has_intersection = check_intersection((x0, y0), (dx, dy), seg)
        if has_intersection:
            intersection_count += 1
            break

# print(f'Part 1: {intersection_count}')
