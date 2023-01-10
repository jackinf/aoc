import math


def solve(bin_val):
    version = int(bin_val[:3], 2)
    type_id = bin_val[3:6]

    # type_id 4 => literal value
    if int(type_id, 2) == 4:
        # add leading zero's to the right so that the length is divisible by 4
        # bin_val = bin_val.ljust(math.ceil(len(bin_val) / 4) * 4, '0')

        curr = 6
        literal_val = ''
        while True:
            group = bin_val[curr:curr+5]
            curr += 5
            literal_val += group[1:5]
            if group[0] == '0':
                break

        return version, curr
        # return literal_val

    # type_id other => operator type
    else:
        length = 15 if bin_val[6] == '0' else 11
        length_of_sub_packets = int(bin_val[7:7+length], 2)

        versions = [version]
        curr = 7 + length
        while length_of_sub_packets > 0:
            version, offset = solve(bin_val[curr:])
            length_of_sub_packets -= offset
            curr += offset
            versions.append(version)

        return sum(versions), curr


if __name__ == '__main__':
    # with open('input.txt') as f:
    #     hex = f.readline().strip()
    # hex = '8A004A801A8002F478'
    hex = '620080001611562C8802118E34'
    # hex = 'D2FE28'
    # hex = 'EE00D40C823060'

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

    res, offset = solve(bin_val)

    print(f'Result 1: {res}')

    # '111000000000000110111101000101001010010001001000000000'
    # '00111000000000000110111101000101001010010001001000000000'