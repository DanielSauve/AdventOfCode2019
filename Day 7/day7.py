def calculate_modes(instruction):
    modes = []
    instruction = instruction // 100
    modes.append(instruction % 10 == 1)
    instruction = instruction // 10
    modes.append(instruction % 10 == 1)
    instruction = instruction // 10
    modes.append(instruction % 10 == 1)
    return modes


def run(prog, inp):
    curr = 0
    curr_inp = 0
    while prog[curr] != 99:
        instruction = prog[curr]
        modes = calculate_modes(instruction)
        if instruction % 10 == 1:
            val1 = prog[curr + 1] if modes[0] else prog[prog[curr + 1]]
            val2 = prog[curr + 2] if modes[1] else prog[prog[curr + 2]]
            out = prog[curr + 3]
            try:
                prog[out] = val1 + val2
            except:
                return
            curr += 4
        elif instruction % 10 == 2:
            val1 = prog[curr + 1] if modes[0] else prog[prog[curr + 1]]
            val2 = prog[curr + 2] if modes[1] else prog[prog[curr + 2]]
            out = prog[curr + 3]
            try:
                prog[out] = val1 * val2
            except:
                return
            curr += 4
        elif instruction % 10 == 3:
            prog[prog[curr + 1]] = inp[curr_inp]
            curr_inp += 1
            curr += 2
        elif instruction % 10 == 4:
            return prog[curr + 1] if modes[0] else prog[prog[curr + 1]]
        elif instruction % 10 == 5:
            val = prog[curr + 1] if modes[0] else prog[prog[curr + 1]]
            if val != 0:
                curr = prog[curr + 2] if modes[1] else prog[prog[curr + 2]]
            else:
                curr += 3
        elif instruction % 10 == 6:
            val = prog[curr + 1] if modes[0] else prog[prog[curr + 1]]
            if val == 0:
                curr = prog[curr + 2] if modes[1] else prog[prog[curr + 2]]
            else:
                curr += 3
        elif instruction % 10 == 7:
            val1 = prog[curr + 1] if modes[0] else prog[prog[curr + 1]]
            val2 = prog[curr + 2] if modes[1] else prog[prog[curr + 2]]
            out = prog[curr + 3]
            prog[out] = 1 if val1 < val2 else 0
            curr += 4
        elif instruction % 10 == 8:
            val1 = prog[curr + 1] if modes[0] else prog[prog[curr + 1]]
            val2 = prog[curr + 2] if modes[1] else prog[prog[curr + 2]]
            out = prog[curr + 3]
            prog[out] = 1 if val1 == val2 else 0
            curr += 4


def code_to_prog(code):
    return [int(x) for x in code.split(",")]


def gen_phases():
    out = []
    for i in range(43211):
        s = str(i)
        if "1" in s and "2" in s and "3" in s and "4" in s and "0" in s:
            out.append([int(x) for x in s])
    return out


if __name__ == "__main__":
    f = open("day7.txt").read()
    phases = gen_phases()
    max_signal = 0
    phase_combo = phases[0]
    for phase in phases:
        output = 0
        for amp in phase:
            prog = code_to_prog(f)
            output = run(prog, [amp, output])
        if output > max_signal:
            max_signal = output
            phase_combo = phase
    print(max_signal)
    print(phase_combo)
