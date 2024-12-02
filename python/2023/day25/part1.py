import math
from collections import defaultdict

import networkx as nx
from matplotlib import pyplot as plt

with open('input.txt', 'r') as f:
    lines = [line.split(':') for line in f.read().split('\n')]
    lines = {part[0]: part[1].split() for part in lines}


print(lines)


def draw_graph(data):
    # Create a new graph
    G = nx.Graph()

    # Add nodes and edges from the data
    for node, edges in data.items():
        for edge in edges:
            G.add_edge(node, edge)

    # Draw the graph
    plt.figure(figsize=(10, 8))
    nx.draw(G, with_labels=True, node_color='lightblue', node_size=2000, edge_color='gray', linewidths=1.5, font_size=10)
    plt.show()


draw_graph(lines)  # takes a bit of time to build the graph and draw it

# Well, I just visualized the solution, and I immediately saw on a picture the three weakly connected nodes. So I just
# modified the input by removing them.
with open('input_modified.txt', 'r') as f:
    lines = [line.split(':') for line in f.read().split('\n')]
    lines = {part[0]: part[1].split() for part in lines}


# get all nodes
all_nodes = set()
for node, neighbors in lines.items():
    all_nodes.add(node)
    for nei in neighbors:
        all_nodes.add(nei)


# graph with bi-directional nodes
lines2 = defaultdict(set)
for node, neighbors in lines.items():
    for nei in neighbors:
        lines2[node].add(nei)
        lines2[nei].add(node)
lines = lines2
print(lines)


# get separated groups
groups = {}
group_index = 0

for group_index, node in enumerate(all_nodes):
    if node in groups:
        continue

    q = [node]
    while q:
        curr = q.pop(0)

        if curr in groups:
            continue
        groups[curr] = group_index

        for nei in lines.get(curr, []):
            q.append(nei)

print(groups)
from collections import Counter
group_counts = Counter(Counter(groups).values()).values()
total = math.prod(group_counts)

print(f'Part 1: {total}')
