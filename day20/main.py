from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Node:
    val: int
    prev: Optional["Node"]
    next: Optional["Node"]


def construct_doubly_linked_list(numbers: List[int]):
    head = Node(val=0, prev=None, next=None)
    queue = []
    prev = head
    for number in numbers:
        node = Node(val=number, prev=prev, next=None)
        queue.append(node)
        prev.next = node
        prev = node
    prev.next, head.next.prev = head.next, prev

    return head, queue


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


def shuffle(queue):
    for node in queue:
        steps = node.val

        while steps < 0:
            steps += 1
            swap_nodes(node.prev, node)

        while steps > 0:
            steps -= 1
            swap_nodes(node, node.next)


def calculate_result(head: Node):
    # find 0 as starting position
    node = head.next
    while node.val != 0:
        node = node.next

    # find 1000th, 2000th and 3000th elements
    steps, result = 0, 0
    while steps <= 3000:
        node = node.next
        steps += 1

        if steps % 1000 == 0:
            result += node.val
    return result


if __name__ == '__main__':
    with open('input.txt') as f:
        numbers = [int(line.strip()) for line in f]

    head, queue1 = construct_doubly_linked_list(numbers)
    shuffle(queue1)
    res1 = calculate_result(head)
    print(f'Result 1: {res1}')

    head, queue2 = construct_doubly_linked_list(numbers)
    for _ in range(10):  # I think that this is not right
        shuffle(queue2)
    res2 = calculate_result(head) * 811589153

    print(f'Result 2: {res2}')



