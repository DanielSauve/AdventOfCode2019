def calculate_modes(instruction):
    modes = []
    instruction = instruction // 100
    modes.append(instruction % 10)
    instruction = instruction // 10
    modes.append(instruction % 10)
    instruction = instruction // 10
    modes.append(instruction % 10)
    return modes


def run(prog, grid):
    curr = 0
    relative_base = 0
    curr_x, curr_y = 0, 0
    grid[(curr_x, curr_y)] = (0, ".")
    i = 0
    dist = 0
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
            if (curr_x, curr_y + 1) not in grid:
                i = 1
            elif (curr_x, curr_y - 1) not in grid:
                i = 2
            elif (curr_x + 1, curr_y) not in grid:
                i = 4
            elif (curr_x - 1, curr_y) not in grid:
                i = 3
            else:
                d, _ = grid[curr_x, curr_y + 1]
                if d != -1 and d < dist:
                    i = 1
                d, _ = grid[curr_x, curr_y - 1]
                if d != -1 and d < dist:
                    i = 2
                d, _ = grid[curr_x - 1, curr_y]
                if d != -1 and d < dist:
                    i = 3
                d, _ = grid[curr_x + 1, curr_y]
                if d != -1 and d < dist:
                    i = 4
                if dist == 0:
                    return
            if modes[0] == 0:
                prog[prog[curr + 1]] = i
            elif modes[0] == 2:
                prog[relative_base + prog[curr + 1]] = i
            curr += 2
        elif instruction % 10 == 4:
            o = prog[curr + 1] if modes[0] == 1 else prog[prog[curr + 1]] if modes[0] == 0 else prog[
                relative_base + prog[curr + 1]]
            if o == 0:
                if i == 1:
                    grid[(curr_x, curr_y + 1)] = (-1, "#")
                elif i == 2:
                    grid[(curr_x, curr_y - 1)] = (-1, "#")
                elif i == 3:
                    grid[(curr_x - 1, curr_y)] = (-1, "#")
                elif i == 4:
                    grid[(curr_x + 1, curr_y)] = (-1, "#")
            elif o == 1:
                if i == 1:
                    if (curr_x, curr_y + 1) not in grid:
                        grid[(curr_x, curr_y + 1)] = (dist + 1, ".")
                    dist, _ = grid[curr_x, curr_y + 1]
                    curr_y += 1
                elif i == 2:
                    if (curr_x, curr_y - 1) not in grid:
                        grid[(curr_x, curr_y - 1)] = (dist + 1, ".")
                    dist, _ = grid[(curr_x, curr_y - 1)]
                    curr_y -= 1
                elif i == 3:
                    if (curr_x - 1, curr_y) not in grid:
                        grid[(curr_x - 1, curr_y)] = (dist + 1, ".")
                    dist, _ = grid[(curr_x - 1, curr_y)]
                    curr_x -= 1
                elif i == 4:
                    if (curr_x + 1, curr_y) not in grid:
                        grid[(curr_x + 1, curr_y)] = (dist + 1, ".")
                    dist, _ = grid[(curr_x + 1, curr_y)]
                    curr_x += 1
            elif o == 2:
                if i == 1:
                    if (curr_x, curr_y + 1) not in grid:
                        grid[(curr_x, curr_y + 1)] = (dist + 1, "O")
                    dist, _ = grid[curr_x, curr_y + 1]
                    curr_y += 1
                elif i == 2:
                    if (curr_x, curr_y - 1) not in grid:
                        grid[(curr_x, curr_y - 1)] = (dist + 1, "O")
                    dist, _ = grid[(curr_x, curr_y - 1)]
                    curr_y -= 1
                elif i == 3:
                    if (curr_x - 1, curr_y) not in grid:
                        grid[(curr_x - 1, curr_y)] = (dist + 1, "O")
                    dist, _ = grid[(curr_x - 1, curr_y)]
                    curr_x -= 1
                elif i == 4:
                    if (curr_x + 1, curr_y) not in grid:
                        grid[(curr_x + 1, curr_y)] = (dist + 1, "O")
                    dist, _ = grid[(curr_x + 1, curr_y)]
                    curr_x += 1
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
    f = open("day15.txt").read()
    prog = code_to_prog(f)
    prog.extend([0 for _ in range(10000)])
    grid = dict()
    run(prog, grid)
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
    for y in range(min_y, max_y):
        m.append([])
        for x in range(min_x, max_x):
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
