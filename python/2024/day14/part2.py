import glob
import time
from collections import Counter
from typing import Tuple, List
import tkinter as tk
from PIL import ImageGrab, Image

DEBUG = False
WIDTH = 101  # width
HEIGHT = 103  # height
MAX_SECONDS = 100
CELL_SIZE = 5

type ROBOT = Tuple[int, int, int, int]
type ROBOTS = List[ROBOT]
type Q4_SAFETY = List[int]


def draw_grid(canvas, state):
    canvas.delete("all")  # Clear the canvas
    counter = Counter([(px, py) for px, py, vx, vy in state])

    for (col, row), count in counter.items():
        x1, y1 = col * CELL_SIZE, row * CELL_SIZE
        x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
        canvas.create_rectangle(x1, y1, x2, y2, fill="green", outline="")


def read_input() -> ROBOTS:
    with open('input.txt') as f:
        lines = f.read().split('\n')

    robots = []
    for line in lines:
        left, right = line.split()
        col, row = [int(val) for val in left[2:].split(',')]
        col_delta, row_delta = [int(val) for val in right[2:].split(',')]

        robots.append((col, row, col_delta, row_delta))

    return robots


def step(state1: ROBOTS, size = 1) -> ROBOTS:
    state2: ROBOTS = []
    for col, row, col_delta, row_delta in state1:
        col += (col_delta * size)
        col %= WIDTH
        row += (row_delta * size)
        row %= HEIGHT
        state2.append((col, row, col_delta, row_delta))
    return state2


def save_frame(canvas, second):
    # Get the canvas position in the root window
    canvas.update()  # Ensure the canvas is updated
    x = canvas.winfo_rootx()
    y = canvas.winfo_rooty()
    w = x + canvas.winfo_width()
    h = y + canvas.winfo_height()

    # Take a screenshot of the canvas area
    img = ImageGrab.grab(bbox=(x, y, w, h))
    img.save(f"{second}.jpg")


def create_gif(output_filename="simulation.gif", frame_duration=24, long_frame_index=78, long_frame_duration=3000):
    frames = sorted(glob.glob("*.jpg"), key=lambda x: int(x.split('.')[0]))
    images = [Image.open(frame) for frame in frames]

    # Modify durations for each frame
    durations = [frame_duration] * len(images)
    if 0 <= long_frame_index < len(durations):
        durations[long_frame_index] = long_frame_duration  # Set longer duration for the specified frame

    # Save as GIF
    images[0].save(
        output_filename,
        save_all=True,
        append_images=images[1:],
        duration=durations,  # Pass the list of durations
        loop=0  # Infinite loop
    )
    print(f"GIF saved as {output_filename}")



START = 74
STEP_SIZE_TREE = 101
ANSWER = 78  # i found this frame by manually inspecting screenshots

def run():
    robots = read_input()

    root = tk.Tk()
    root.title("Robot Grid Simulation")
    canvas = tk.Canvas(root, width=WIDTH * CELL_SIZE, height=HEIGHT * CELL_SIZE, bg="white")
    canvas.pack()

    for _ in range(START):
        robots = step(robots, size=1)

    for second in range(MAX_SECONDS):
        robots = step(robots, size=STEP_SIZE_TREE)
        draw_grid(canvas, robots)
        save_frame(canvas, second)
        time.sleep(0.1)

    create_gif(long_frame_index=ANSWER)

run()