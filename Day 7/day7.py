from intcode import Intcode, AbstractIntcodeIO, code_to_prog


class AmplifierIntcodeIO(AbstractIntcodeIO):
    def __init__(self, input_buffer, output_buffer):
        self.input_pointer = 0
        self.input_buffer = input_buffer
        self.output_buffer = output_buffer

    def input(self):
        if self.input_pointer == len(self.input_buffer):
            return False
        out = self.input_buffer[self.input_pointer]
        self.input_pointer += 1
        return out

    def output(self, out):
        self.output_buffer.append(out)


def gen_phases_1():
    out = []
    for i in range(43211):
        s = str(i)
        if "1" in s and "2" in s and "3" in s and "4" in s and "0" in s:
            out.append([int(x) for x in s])
    return out


def gen_phases_2():
    out = []
    for i in range(56789, 98766):
        s = str(i)
        if "5" in s and "6" in s and "7" in s and "8" in s and "9" in s:
            out.append([int(x) for x in s])
    return out


if __name__ == "__main__":
    f = open("day7.txt").read()
    phases = gen_phases_1()
    max_signal = 0
    phase_combo = phases[0]
    for phase in phases:
        output = 0
        for amp in phase:
            inp = [amp, output]
            out = []
            io = AmplifierIntcodeIO(inp, out)
            prog = code_to_prog(f)
            intcode = Intcode(prog, io)
            intcode.run()
            output = out[0]
        if output > max_signal:
            max_signal = output
            phase_combo = phase
    print(max_signal)
    print(phase_combo)

    phases = gen_phases_2()
    max_signal = 0
    phase_combo = phases[0]
    for phase in phases:
        print(phase)
        amplifiers = []
        buffers = [[x] for x in phase]
        buffers[-1].append(0)
        for i in range(len(buffers)):
            io = AmplifierIntcodeIO(buffers[i - 1], buffers[i])
            prog = code_to_prog(f)
            prog.extend([0 for _ in range(10000)])
            amplifiers.append(Intcode(prog, io))
        finished_count = 0
        curr_amp = 0
        while finished_count != 5:
            state = amplifiers[curr_amp].run()
            if state:
                finished_count += 1
            curr_amp = (curr_amp + 1) % 5
        if buffers[-1][-1] > max_signal:
            max_signal = buffers[-1][-1]
            phase_combo = phase
    print(max_signal)
    print(phase_combo)
