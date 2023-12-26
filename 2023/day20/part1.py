from typing import Optional

with open('sample1.txt', 'r') as f:
    lines = f.read().split('\n')

lines = [line.split('->') for line in lines]
lines = {x[0].strip(): [y.strip() for y in x[1].strip().split(',')] for x in lines}


# is_flip_flop = lambda node: f'%{nei}' in lines
# is_conjunction = lambda node: f'%{nei}' in lines


# def get_pulse(node) -> Optional[str]:
#     if node == "broadcaster":
#         return "low"
#
#     if is_flip_flop(node):
#         if pulse == "high":
#             return None
#         return "low"
#
#     if is_conjunction(node):


def debug(curr, pulse, nei):
    print(f'{curr} -{pulse} -> {nei}')


# print(lines)
# cycle = 1
# while cycle <= 1:
#
#     q = [('broadcaster', 'low')]
#     while q:
#         curr, pulse = q.pop(0)
#
#         for nei in lines[curr]:
#             # is it flip-flop module
#             if f'%{nei}' in lines:
#                 q.append((nei, pulse))
#                 debug(curr, pulse, nei)
#             # is it conjuction module
#             elif f'&{nei}' in lines:
#                 new_pulse = "high" if pulse == "low" else "low"
#                 q.append((nei, pulse))
#                 debug(curr, pulse, nei)


