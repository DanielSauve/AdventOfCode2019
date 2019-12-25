from intcode import Intcode, code_to_prog, AbstractIntcodeIO


class PinballIntcodeIO(AbstractIntcodeIO):
    def __init__(self):
        self.buffer = []
        self.ball = (0, 0)
        self.paddle = (0, 0)

    def input(self):
        ball_x, _ = self.ball
        paddle_x, _ = self.paddle
        return 0 if ball_x == paddle_x else 1 if ball_x > paddle_x else -1

    def output(self, out):
        self.buffer.append(out)
        if len(self.buffer) % 3 == 0:
            if out == 4:
                self.ball = (self.buffer[-3], self.buffer[-2])
            if out == 3:
                self.paddle = (self.buffer[-3], self.buffer[-2])


if __name__ == "__main__":
    f = open("day13.txt").read()
    prog = code_to_prog(f)
    prog.extend([0 for _ in range(10000)])
    io = PinballIntcodeIO()
    intcode = Intcode(prog, io)
    intcode.run()
    grid = dict()
    for i in range(0, len(io.buffer), 3):
        x, y, tile = io.buffer[i:i + 3]
        grid[(x, y)] = tile
    print(list(grid.values()).count(2))
    prog = code_to_prog(f)
    prog.extend([0 for _ in range(10000)])
    prog[0] = 2
    io = PinballIntcodeIO()
    intcode = Intcode(prog, io)
    intcode.run()
    print(io.buffer[-1])
