import math


class Day17:
    def solve(self, program, reg_a, reg_b, reg_c):
        ins_ptr = 0

        def combo_op(op):
            if 0 <= op <= 3: return op
            if op == 4: return reg_a
            if op == 5: return reg_b
            if op == 6: return reg_c
            if op == 7: raise Exception('reserved')

        output = []
        while len(program) > ins_ptr:
            opcode = program[ins_ptr]
            operand = program[ins_ptr + 1]

            match opcode:
                # adv - A registry division by 2 in power of something
                case 0:
                    reg_a = reg_a // int(math.pow(2, combo_op(operand)))
                    ins_ptr += 2

                # bxl - B registry bitwise XOR
                case 1:
                    reg_b ^= operand
                    ins_ptr += 2

                # bst - B registry combo operand value
                case 2:
                    reg_b = combo_op(operand) % 8
                    ins_ptr += 2

                # jnz
                case 3:
                    if reg_a != 0:
                        ins_ptr = operand
                    else:
                        ins_ptr += 2

                # bxc - B registry and C registry bitwise XOR
                case 4:
                    reg_b ^= reg_c
                    ins_ptr += 2

                # out - print the value
                case 5:
                    output.append(combo_op(operand) % 8)
                    ins_ptr += 2

                # bdv
                case 6:
                    reg_b = reg_a // int(math.pow(2, combo_op(operand)))
                    ins_ptr += 2

                # cdv
                case 7:
                    reg_c = reg_a // int(math.pow(2, combo_op(operand)))
                    ins_ptr += 2

        # print(f'registries: A={reg_a} B={reg_b} C={reg_c}')

        if len(output) == 0:
            return None

        return output


def shuffle_different_solutions(program, a_reg, nth_digit):
    val = program[-nth_digit]

    # go through all 3-bit numbers
    for i in range(8):
        output = Day17().solve(program, a_reg + i, 0, 0)
        if output[0] != val:
            continue

        if nth_digit == len(program):
            return a_reg + i

        if nth_digit < len(program):
            res = shuffle_different_solutions(program, (a_reg + i) * 8, nth_digit + 1)
            if res:
                return res


if __name__ == '__main__':
    # example 1:
    # print(shuffle_different_solutions([0, 3, 5, 4, 3, 0], 0, 1))

    # 000 = 0
    # 000 = 0
    # 011 = 3
    # 101 = 5
    # 100 = 4
    # 011 = 3

    # therefore, 011 + 100 + 101 + 011 + 000 + 000 => 011100101011000000 => int('011100101011000000', 2) = 117440

    # example 2:
    # print(shuffle_different_solutions([2, 3, 5, 4, 3, 6], 0, 1))
    # should be ['110', '011', '100', '101', '011', '010'] as it goes from end to start

    # part 2:
    print('Part 2:')
    my_input = [2, 4, 1, 7, 7, 5, 0, 3, 4, 0, 1, 7, 5, 5, 3, 0]
    print(shuffle_different_solutions(my_input, 0, 1))