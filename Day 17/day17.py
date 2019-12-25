from intcode import Intcode, AbstractIntcodeIO, code_to_prog


class ASCIIIntcodeIO(AbstractIntcodeIO):
    def __init__(self, grid):
        self.grid = grid

    def input(self):
        pass

    def output(self, out):
        self.grid.append(chr(out))


if __name__ == "__main__":
    f = open("day17.txt").read()
    prog = code_to_prog(f)
    prog.extend([0 for _ in range(10000)])
    grid = []
    io = ASCIIIntcodeIO(grid)
    intcode = Intcode(prog, io)
    intcode.run()
    scaffolding = [[]]
    for item in grid:
        if item == "\n":
            scaffolding.append([])
        else:
            scaffolding[-1].append(item)
    while not scaffolding[-1]:
        scaffolding.pop()
    alignment_sum = 0
    for y in range(1, len(scaffolding) - 1):
        for x in range(1, len(scaffolding[y]) - 1):
            if scaffolding[y][x] == "#" and scaffolding[y + 1][x] == "#" and scaffolding[y - 1][x] == "#" and \
                    scaffolding[y][x + 1] == "#" and scaffolding[y][x - 1] == "#":
                alignment_sum += x * y
    print(alignment_sum)
