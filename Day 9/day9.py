def calculate_modes(instruction):
    modes = []
    instruction = instruction // 100
    modes.append(instruction % 10)
    instruction = instruction // 10
    modes.append(instruction % 10)
    instruction = instruction // 10
    modes.append(instruction % 10)
    return modes


def run(prog):
    curr = 0
    relative_base = 0
    while prog[curr] != 99:
        instruction = prog[curr]
        modes = calculate_modes(instruction)
        if instruction % 10 == 1:
            val1 = prog[curr + 1] if modes[0] == 1 else prog[prog[curr + 1]] if modes[0] == 0 else prog[
                relative_base + prog[curr + 1]]
            val2 = prog[curr + 2] if modes[1] == 1 else prog[prog[curr + 2]] if modes[1] == 0 else prog[
                relative_base + prog[curr + 2]]
            out = prog[curr + 3] if modes[2] == 0 else relative_base + prog[curr + 3]
            try:
                prog[out] = val1 + val2
            except:
                return
            curr += 4
        elif instruction % 10 == 2:
            val1 = prog[curr + 1] if modes[0] == 1 else prog[prog[curr + 1]] if modes[0] == 0 else prog[
                relative_base + prog[curr + 1]]
            val2 = prog[curr + 2] if modes[1] == 1 else prog[prog[curr + 2]] if modes[1] == 0 else prog[
                relative_base + prog[curr + 2]]
            out = prog[curr + 3] if modes[2] == 0 else relative_base + prog[curr + 3]
            try:
                prog[out] = val1 * val2
            except:
                return
            curr += 4
        elif instruction % 10 == 3:
            if modes[0] == 0:
                prog[prog[curr + 1]] = int(input("Please input a number: "))
            elif modes[0] == 2:
                prog[relative_base + prog[curr + 1]] = int(input("Please input a number: "))
            curr += 2
        elif instruction % 10 == 4:
            print(prog[curr + 1] if modes[0] == 1 else prog[prog[curr + 1]] if modes[0] == 0 else prog[
                relative_base + prog[curr + 1]])
            curr += 2
        elif instruction % 10 == 5:
            val = prog[curr + 1] if modes[0] == 1 else prog[prog[curr + 1]] if modes[0] == 0 else prog[
                relative_base + prog[curr + 1]]
            if val != 0:
                curr = prog[curr + 2] if modes[1] == 1 else prog[prog[curr + 2]] if modes[1] == 0 else prog[
                    relative_base + prog[curr + 2]]
            else:
                curr += 3
        elif instruction % 10 == 6:
            val = prog[curr + 1] if modes[0] == 1 else prog[prog[curr + 1]] if modes[0] == 0 else prog[
                relative_base + prog[curr + 1]]
            if val == 0:
                curr = prog[curr + 2] if modes[1] == 1 else prog[prog[curr + 2]] if modes[0] == 0 else prog[
                    relative_base + prog[curr + 2]]
            else:
                curr += 3
        elif instruction % 10 == 7:
            val1 = prog[curr + 1] if modes[0] == 1 else prog[prog[curr + 1]] if modes[0] == 0 else prog[
                relative_base + prog[curr + 1]]
            val2 = prog[curr + 2] if modes[1] == 1 else prog[prog[curr + 2]] if modes[1] == 0 else prog[
                relative_base + prog[curr + 2]]
            out = prog[curr + 3] if modes[2] == 0 else relative_base + prog[curr + 3]
            prog[out] = 1 if val1 < val2 else 0
            curr += 4
        elif instruction % 10 == 8:
            val1 = prog[curr + 1] if modes[0] == 1 else prog[prog[curr + 1]] if modes[0] == 0 else prog[
                relative_base + prog[curr + 1]]
            val2 = prog[curr + 2] if modes[1] == 1 else prog[prog[curr + 2]] if modes[1] == 0 else prog[
                relative_base + prog[curr + 2]]
            out = prog[curr + 3] if modes[2] == 0 else relative_base + prog[curr + 3]
            prog[out] = 1 if val1 == val2 else 0
            curr += 4
        elif instruction % 10 == 9:
            val = prog[curr + 1] if modes[0] == 1 else prog[prog[curr + 1]] if modes[0] == 0 else prog[
                relative_base + prog[curr + 1]]
            relative_base += val
            curr += 2


def code_to_prog(code):
    return [int(x) for x in code.split(",")]


if __name__ == "__main__":
    f = open("day9.txt").read()
    prog = code_to_prog(f)
    prog.extend([0 for _ in range(10000)])
    run(prog)
