def calculate_modes(instruction):
    modes = []
    instruction = instruction // 100
    modes.append(instruction % 10 == 1)
    instruction = instruction // 10
    modes.append(instruction % 10 == 1)
    instruction = instruction // 10
    modes.append(instruction % 10 == 1)
    return modes


def run(prog):
    curr = 0
    while prog[curr] != 99:
        instruction = prog[curr]
        if instruction % 10 == 1:
            modes = calculate_modes(instruction)
            val1 = prog[curr + 1] if modes[0] else prog[prog[curr + 1]]
            val2 = prog[curr + 2] if modes[1] else prog[prog[curr + 2]]
            out = prog[curr + 3]
            try:
                prog[out] = val1 + val2
            except:
                return
            curr += 4
        elif instruction % 10 == 2:
            modes = calculate_modes(instruction)
            val1 = prog[curr + 1] if modes[0] else prog[prog[curr + 1]]
            val2 = prog[curr + 2] if modes[1] else prog[prog[curr + 2]]
            out = prog[curr + 3]
            try:
                prog[out] = val1 * val2
            except:
                return
            curr += 4
        elif instruction % 10 == 3:
            prog[prog[curr + 1]] = int(input("Please input a value: "))
            curr += 2
        elif instruction % 10 == 4:
            print(prog[prog[curr + 1]])
            curr += 2
    return prog[0]


def code_to_prog(code):
    return [int(x) for x in code.split(",")]


if __name__ == "__main__":
    f = open("day5.txt").read()
    prog = code_to_prog(f)
    run(prog)
