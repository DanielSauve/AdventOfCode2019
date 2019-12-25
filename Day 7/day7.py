from intcode import Intcode, AbstractIntcodeIO, code_to_prog


class AmplifierIntcodeIO(AbstractIntcodeIO):
    def __init__(self, input_buffer, output_buffer):
        self.input_pointer = 0
        self.input_buffer = input_buffer
        self.output_buffer = output_buffer

    def input(self):
        out = self.input_buffer[self.input_pointer]
        self.input_pointer += 1
        return out

    def output(self, out):
        self.output_buffer.append(out)


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
