from intcode import Intcode, AbstractIntcodeIO, code_to_prog


class RepairIntcodeIO(AbstractIntcodeIO):
    def __init__(self, grid):
        self.grid = grid
        self.grid[(0, 0)] = (0, ".")
        self.dir = 0
        self.dist = 0
        self.curr_x = 0
        self.curr_y = 0

    def input(self):
        if (self.curr_x, self.curr_y + 1) not in self.grid:
            self.dir = 1
        elif (self.curr_x, self.curr_y - 1) not in self.grid:
            self.dir = 2
        elif (self.curr_x + 1, self.curr_y) not in self.grid:
            self.dir = 4
        elif (self.curr_x - 1, self.curr_y) not in self.grid:
            self.dir = 3
        else:
            d, _ = self.grid[self.curr_x, self.curr_y + 1]
            if d != -1 and d < self.dist:
                self.dir = 1
            d, _ = self.grid[self.curr_x, self.curr_y - 1]
            if d != -1 and d < self.dist:
                self.dir = 2
            d, _ = self.grid[self.curr_x - 1, self.curr_y]
            if d != -1 and d < self.dist:
                self.dir = 3
            d, _ = self.grid[self.curr_x + 1, self.curr_y]
            if d != -1 and d < self.dist:
                self.dir = 4
            if self.dist == 0:
                return False
        return self.dir

    def output(self, out):
        if out == 0:
            if self.dir == 1:
                self.grid[(self.curr_x, self.curr_y + 1)] = (-1, "#")
            elif self.dir == 2:
                self.grid[(self.curr_x, self.curr_y - 1)] = (-1, "#")
            elif self.dir == 3:
                self.grid[(self.curr_x - 1, self.curr_y)] = (-1, "#")
            elif self.dir == 4:
                self.grid[(self.curr_x + 1, self.curr_y)] = (-1, "#")
        elif out == 1:
            if self.dir == 1:
                if (self.curr_x, self.curr_y + 1) not in self.grid:
                    self.grid[(self.curr_x, self.curr_y + 1)] = (self.dist + 1, ".")
                self.dist, _ = self.grid[self.curr_x, self.curr_y + 1]
                self.curr_y += 1
            elif self.dir == 2:
                if (self.curr_x, self.curr_y - 1) not in self.grid:
                    self.grid[(self.curr_x, self.curr_y - 1)] = (self.dist + 1, ".")
                self.dist, _ = self.grid[(self.curr_x, self.curr_y - 1)]
                self.curr_y -= 1
            elif self.dir == 3:
                if (self.curr_x - 1, self.curr_y) not in self.grid:
                    self.grid[(self.curr_x - 1, self.curr_y)] = (self.dist + 1, ".")
                self.dist, _ = self.grid[(self.curr_x - 1, self.curr_y)]
                self.curr_x -= 1
            elif self.dir == 4:
                if (self.curr_x + 1, self.curr_y) not in self.grid:
                    self.grid[(self.curr_x + 1, self.curr_y)] = (self.dist + 1, ".")
                self.dist, _ = self.grid[(self.curr_x + 1, self.curr_y)]
                self.curr_x += 1
        elif out == 2:
            if self.dir == 1:
                if (self.curr_x, self.curr_y + 1) not in self.grid:
                    self.grid[(self.curr_x, self.curr_y + 1)] = (self.dist + 1, "O")
                self.dist, _ = self.grid[self.curr_x, self.curr_y + 1]
                self.curr_y += 1
            elif self.dir == 2:
                if (self.curr_x, self.curr_y - 1) not in self.grid:
                    self.grid[(self.curr_x, self.curr_y - 1)] = (self.dist + 1, "O")
                self.dist, _ = self.grid[(self.curr_x, self.curr_y - 1)]
                self.curr_y -= 1
            elif self.dir == 3:
                if (self.curr_x - 1, self.curr_y) not in self.grid:
                    self.grid[(self.curr_x - 1, self.curr_y)] = (self.dist + 1, "O")
                self.dist, _ = self.grid[(self.curr_x - 1, self.curr_y)]
                self.curr_x -= 1
            elif self.dir == 4:
                if (self.curr_x + 1, self.curr_y) not in self.grid:
                    self.grid[(self.curr_x + 1, self.curr_y)] = (self.dist + 1, "O")
                self.dist, _ = self.grid[(self.curr_x + 1, self.curr_y)]
                self.curr_x += 1


if __name__ == "__main__":
    f = open("day15.txt").read()
    prog = code_to_prog(f)
    prog.extend([0 for _ in range(10000)])
    grid = dict()
    io = RepairIntcodeIO(grid)
    intcode = Intcode(prog, io)
    intcode.run()
    oxygen = -1
    for dist, tile in grid.values():
        if tile == "O":
            print(dist)
            oxygen = dist
    max_dist, _ = max(grid.values())
    max_x, max_y, min_x, min_y = 0, 0, 0, 0
    for x, y in grid.keys():
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        min_x = min(min_x, x)
        min_y = min(min_y, y)
    m = []
    for y in range(min_y, max_y + 1):
        m.append([])
        for x in range(min_x, max_x + 1):
            tile = "#"
            if (x, y) in grid:
                _, tile = grid[(x, y)]
            m[-1].append(tile)
    start_x, start_y = -1, -1
    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == "O":
                start_x, start_y = x, y
    queue = []
    seen = set()
    max_dist = -1
    curr_dist = 0
    queue.append((start_x, start_y, curr_dist))
    while len(queue) > 0:
        curr_x, curr_y, curr_dist = queue.pop()
        max_dist = max(max_dist, curr_dist)
        seen.add((curr_x, curr_y))
        try:
            if m[curr_y][curr_x + 1] != "#" and (curr_x + 1, curr_y) not in seen:
                queue.append((curr_x + 1, curr_y, curr_dist + 1))
        except IndexError:
            pass
        try:
            if m[curr_y][curr_x - 1] != "#" and (curr_x - 1, curr_y) not in seen:
                queue.append((curr_x - 1, curr_y, curr_dist + 1))
        except IndexError:
            pass
        try:
            if m[curr_y + 1][curr_x] != "#" and (curr_x, curr_y + 1) not in seen:
                queue.append((curr_x, curr_y + 1, curr_dist + 1))
        except IndexError:
            pass
        try:
            if m[curr_y - 1][curr_x] != "#" and (curr_x, curr_y - 1) not in seen:
                queue.append((curr_x, curr_y - 1, curr_dist + 1))
        except IndexError:
            pass
    print(max_dist)
