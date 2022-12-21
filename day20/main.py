from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    val: int
    prev: Optional["Node"]
    next: Optional["Node"]


def print_nodes(node: Node, steps: int):
    while steps > 0:
        steps -= 1
        print(str(node.val), end=', ')
        node = node.next
    print()


def swap_nodes(left: Node, right: Node):
    a = left.prev
    b = right.next

    a.next, right.prev = right, a
    left.next, b.prev = b, left
    right.next, left.prev = left, right


if __name__ == '__main__':
    with open('input.txt') as f:
        numbers = [int(line.strip()) for line in f]

    N = len(numbers)
    # print(numbers)
    head = Node(val=0, prev=None, next=None)

    queue = []

    # construct doubly linked list
    prev = head
    while numbers:
        number = numbers.pop(0)
        node = Node(val=number, prev=prev, next=None)
        queue.append(node)
        prev.next = node
        prev = node
    prev.next, head.next.prev = head.next, prev

    # print_nodes(head.next, N)

    while queue:
        node = queue.pop(0)
        steps = node.val

        while steps < 0:
            steps += 1
            swap_nodes(node.prev, node)

        while steps > 0:
            steps -= 1
            swap_nodes(node, node.next)

        # print_nodes(head.next, N)

    # find 0 as starting position
    node = head.next
    while node.val != 0:
        node = node.next

    # find 1000th, 2000th and 3000th elements
    steps, res = 0, 0
    while steps <= 3000:
        node = node.next
        steps += 1

        if steps % 1000 == 0:
            res += node.val

    print(f'Result 1: {res}')



