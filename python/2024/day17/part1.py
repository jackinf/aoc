import math

class Day17:
    def solve(self, program, reg_a, reg_b, reg_c):
        print('====')
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

        return ','.join(map(str, output))


if __name__ == '__main__':
    # test data
    print(Day17().solve([2, 6], 0, 0, 9))  # None, reg b = 1
    print(Day17().solve([5, 0, 5, 1, 5, 4], 10, 1, 9))  # 012
    print(Day17().solve([0, 1, 5, 4, 3, 0], 2024, 0, 0))  # 4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0
    print(Day17().solve([1, 7], 0, 29, 0))  # None, reg b = 26
    print(Day17().solve([4, 0], 0, 2024, 43690))  # None, reg b = 44354
    print(Day17().solve([0, 1, 5, 4, 3, 0], 729, 0, 0))  # 4,6,3,5,6,3,5,2,1,0

    # my input
    print(Day17().solve([2, 4, 1, 7, 7, 5, 0, 3, 4, 0, 1, 7, 5, 5, 3, 0], 62769524, 0, 0))