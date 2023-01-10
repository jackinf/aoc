if __name__ == '__main__':
    with open('input.txt') as f:
        hex = f.readline().strip()

    # hex = 'A0016C880162017C3686B18A3D4780'

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

    version_result = 0
    curr = 0
    while curr <= len(bin_val):
        try:
            version_bin = bin_val[curr:curr + 3]
            version = int(version_bin, 2)
            curr += 3  # version skip

            is_literal_bin = bin_val[curr:curr + 3]
            is_literal = int(is_literal_bin, 2) == 4
            curr += 3  # type skip

            if is_literal:
                while True:
                    curr += 5
                    if bin_val[curr - 5] == '0':
                        break
            else:
                len_sector = 15 if bin_val[curr] == '0' else 11
                curr += 1  # length type id skip
                curr += len_sector

            version_result += version
        except:
            break

    print(f'Result 1: {version_result}')
