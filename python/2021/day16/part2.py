import math


def calc(type_id, values):
    match type_id:
        case 0:
            return [sum(values)]
        case 1:
            return [math.prod(values)]
        case 2:
            return [min(values)]
        case 3:
            return [max(values)]
        case 5:
            assert len(values) == 2  # this fails here when I use my input.txt
            return [1 if values[0] > values[1] else 0]
        case 6:
            assert len(values) == 2
            return [1 if values[0] < values[1] else 0]
        case 7:
            assert len(values) == 2
            return [1 if values[0] == values[1] else 0]
        case _:
            raise Exception("should not happen")


def solve(bin_val, pointer: int):
    version_bin = bin_val[pointer:pointer + 3]
    version = int(version_bin, 2)
    pointer += 3  # version skip

    type_id = int(bin_val[pointer:pointer + 3], 2)
    pointer += 3  # type skip
    values = []

    if type_id == 4:
        while True:
            pointer += 5

            values.append(int(bin_val[pointer - 5:pointer], 2))
            if bin_val[pointer - 5] == '0':
                break
        return pointer, version, values

    len_type_id = bin_val[pointer]
    pointer += 1

    if len_type_id == '0':
        diff = int(bin_val[pointer:pointer + 15], 2)
        pointer += 15
        end_pointer = pointer + diff
        while end_pointer != pointer:
            pointer, sub_version, sub_values = solve(bin_val, pointer)
            version += sub_version
            values.extend(sub_values)
    else:
        val = int(bin_val[pointer:pointer + 11], 2)
        pointer += 11
        for _ in range(val):
            pointer, sub_version, sub_values = solve(bin_val, pointer)
            version += sub_version
            values.extend(sub_values)

    values = calc(type_id, values)

    return pointer, version, values


if __name__ == '__main__':
    with open('input.txt') as f:
        hex = f.readline().strip()

    # hex = 'C200B40A82'  # 3
    # hex = '04005AC33890'  # 54
    # hex = '880086C3E88112'  # 7
    # hex = 'CE00C43D881120'  # 9
    # hex = 'D8005AC2A8F0'  # 1
    # hex = 'F600BC2D8F'  # 0
    # hex = '9C005AC2F8F0'  # 0
    # hex = '9C0141080250320F1802104A08'  # 1

    hex_to_bin = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }

    bin_val = ''
    for hex_num in hex:
        bin_val += hex_to_bin[hex_num]

    pointer, version, values = solve(bin_val, 0)
    print(f'Result 2: {values[0]}')  # 248708753 - too low
