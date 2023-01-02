def snafu_to_dec(value: str):
    dec = 0

    for i, ch in enumerate(reversed(value)):
        num = -2 if ch == '=' else -1 if ch == '-' else int(ch)
        five_multiplier = 5 ** i

        dec += num * five_multiplier

    return dec


def dec_to_snafu(dec: int) -> str:
    """
    DEC     SNAFU   Base 5   Base 5 SHIFTED +2
    0         0      0        2
    1         1      1        3
    2         2      2        4

    3        1=      3       10
    4        1-      4       11
    5        10     10       12
    6        11     11       13
    7        12     12       14
    8        2=     13       20
    9        2-     14       21
    10       20     20       22
    11       21     21       23
    12       22     22       24

    13      1==     23      100
    14      1=-     24      101
    15      1=0     30      102
    ...

    DEC = 4890
    base_5_str_arr_shifted = ['3', '4', '11', '2', '10', '2']
    base_5_str_shifted = '01302'

                                2
                              100
                              200
                            11000
                            40000
                           300000
                           ======== +
                           401302

                           ->

                           2=-1=0
    """

    base_5_str = to_base_5(dec)
    base_5_str_arr_shifted = [add_with_base_5(val, '2') for val in list(base_5_str)]

    base_5_res = '0'
    for i, val in enumerate(reversed(base_5_str_arr_shifted)):
        decimals = 10**i
        val2 = str(int(val) * decimals)
        base_5_res = add_with_base_5(base_5_res, val2)

    snafu_str = from_base_5_to_snafu(base_5_res)

    return snafu_str


def from_base_5_to_snafu(base_5: str) -> str:
    snafu = ''
    for val in base_5:
        snafu += from_base_5_to_snafu_single(val)
    return snafu

def from_base_5_to_snafu_single(base_5: str) -> str:
    match base_5:
        case '0': return '='
        case '1': return '-'
        case '2': return '0'
        case '3': return '1'
        case '4': return '2'
        case _: raise Exception('value not supported')


def to_base_5(dec: int):
    res = ''
    while dec:
        res = str(dec % 5) + res
        dec //= 5
    return res


def add_with_base_5(num1_base5: str, num2_base5: str) -> str:
    dec_sum = int(num1_base5, 5) + int(num2_base5, 5)

    return to_base_5(dec_sum)


if __name__ == '__main__':
    with open('input.txt') as f:
        snafus = [line.strip() for line in f]

    mappings = {snafu: snafu_to_dec(snafu) for snafu in snafus}
    dec_result = sum(mappings.values())  # 35798042807410

    part1 = dec_to_snafu(dec_result)  # 2-20=01--0=0=0=2-120
    print(f'Result 1: {part1}')
