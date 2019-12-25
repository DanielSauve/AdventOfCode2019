from intcode import Intcode, AbstractIntcodeIO, code_to_prog


class PaintingIntcodeIO(AbstractIntcodeIO):
    def __init__(self, grid):
        self.grid = grid
        self.curr_x, self.curr_y = 0, 0
        self.curr_dir = 0
        self.curr_out = 0
        self.paint = 0

    def input(self):
        return self.grid.get((self.curr_x, self.curr_y), 0)

    def output(self, out):
        if self.curr_out % 2 == 0:
            self.grid[(self.curr_x, self.curr_y)] = out
            self.paint += 1
        else:
            if out == 1:
                self.curr_dir += 1
            elif out == 0:
                self.curr_dir -= 1
            self.curr_dir = self.curr_dir % 4
            if self.curr_dir == 0:
                self.curr_y += 1
            elif self.curr_dir == 1:
                self.curr_x += 1
            elif self.curr_dir == 2:
                self.curr_y -= 1
            else:
                self.curr_x -= 1
        self.curr_out += 1


if __name__ == "__main__":
    f = open("day11.txt").read()
    prog = code_to_prog(f)
    prog.extend([0 for _ in range(10000)])
    grid = dict()
    io = PaintingIntcodeIO(grid)
    intcode = Intcode(prog, io)
    intcode.run()
    print(len(grid))
    print(io.paint)
    prog = code_to_prog(f)
    prog.extend([0 for _ in range(10000)])
    grid = dict()
    grid[(0, 0)] = 1
    io = PaintingIntcodeIO(grid)
    intcode = Intcode(prog, io)
    intcode.run()
    max_x, max_y, min_x, min_y = 0, 0, 0, 0
    for x, y in grid.keys():
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        min_x = min(min_x, x)
        min_y = min(min_y, y)
    out = []
    # For some reason this is upside down
    for y in range(max_y, min_y - 1, -1):
        out.append([])
        for x in range(min_x, max_x + 1):
            val = grid[(x, y)] if (x, y) in grid else 0
            out[-1].append("." if val == 0 else "#")
    for row in out:
        for val in row:
            print(val, end="")
        print()
