def solve(bin_val, pointer: int):
    version_bin = bin_val[pointer:pointer + 3]
    version = int(version_bin, 2)
    pointer += 3  # version skip

    is_literal_bin = bin_val[pointer:pointer + 3]
    is_literal = int(is_literal_bin, 2) == 4
    pointer += 3  # type skip

    if is_literal:
        while True:
            pointer += 5
            if bin_val[pointer - 5] == '0':
                break
        return pointer, version

    len_type_id = bin_val[pointer]
    pointer += 1

    if len_type_id == '0':
        diff = int(bin_val[pointer:pointer + 15], 2)
        pointer += 15
        end_pointer = pointer + diff
        while end_pointer != pointer:
            pointer, sub_version = solve(bin_val, pointer)
            version += sub_version
    else:
        val = int(bin_val[pointer:pointer + 11], 2)
        pointer += 11
        for _ in range(val):
            pointer, sub_version = solve(bin_val, pointer)
            version += sub_version

    return pointer, version


if __name__ == '__main__':
    with open('input.txt') as f:
        hex = f.readline().strip()

    """
    hex = 620080001611562C8802118E34
    bin = 01100010000000001000000000000000000101100001000101010110001011001000100000000010000100011000111000110100
          VVVTTTILLLLLLLLLLL
    """

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

    pointer, version = solve(bin_val, 0)
    print(f'Result 1: {version}')
