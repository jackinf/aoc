from sympy import symbols, Eq, solve


import matplotlib.pyplot as plt
import matplotlib.patches as patches

with open('input.txt', 'r') as f:
    lines = f.read().split('\n')
    lines = [line.split('@') for line in lines]
    print(lines)


# Rectangle lines
# A, B = 7, 27
A, B = 200000000000000, 400000000000000
POWER = 1
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
    t, u = symbols('t u')

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


def find_intersection_point_between_rays(ray1_start, ray1_direction, ray2_start, ray2_direction):
    # Define the symbols
    t1, t2 = symbols('t1 t2')

    # Parametric equations of the rays
    ray1_x = ray1_start[0] + ray1_direction[0] * t1
    ray1_y = ray1_start[1] + ray1_direction[1] * t1
    ray2_x = ray2_start[0] + ray2_direction[0] * t2
    ray2_y = ray2_start[1] + ray2_direction[1] * t2

    # Equations to solve
    eq1 = Eq(ray1_x, ray2_x)
    eq2 = Eq(ray1_y, ray2_y)

    # Solve the system of equations
    sol = solve((eq1, eq2), (t1, t2))

    # Check if there is a valid intersection
    if sol and t1 in sol and t2 in sol:
        t1_val, t2_val = sol[t1], sol[t2]
        if t1_val.is_real and t2_val.is_real and t1_val >= 0 and t2_val >= 0:
            # Return the intersection coordinates
            return (ray1_x.subs(t1, t1_val), ray1_y.subs(t1, t1_val))
    return None  # No valid intersection


show_drawing()


# Very slow solution
processed = 0
intersection_count = 0
for x0, y0, dx0, dy0 in coordinates:
    for x1, y1, dx1, dy1 in coordinates:
        if x0 == x1 and y0 == y1 and dx0 == dx1 and dy0 == dy1:
            continue
        ray0_start, ray0_dir = (x0, y0), (dx0, dy0)
        ray1_start, ray1_dir = (x1, y1), (dx1, dy1)

        intersection = find_intersection_point_between_rays(ray0_start, ray0_dir, ray1_start, ray1_dir)
        if intersection:
            ix, iy = intersection
            if A <= ix < B and A <= iy <= B:
                intersection_count += 1

    processed += 1
    print(f'Processed: {processed}, intersections: {intersection_count}')

# If ray A intersects ray B, we do intersection_count++ and when ray B intersects ray A, then again intersection_count++
# Therefore, we divide by 2
intersection_count //= 2

print(f'Part 1: {intersection_count}')
