class Moon:
    def __init__(self, x, y, z):
        self.pos = [x, y, z]
        self.vel = [0, 0, 0]

    def calculate_velocity(self, moons):
        for moon in moons:
            self.vel[0] += 1 if self.pos[0] < moon.pos[0] else -1 if self.pos[0] > moon.pos[0] else 0
            self.vel[1] += 1 if self.pos[1] < moon.pos[1] else -1 if self.pos[1] > moon.pos[1] else 0
            self.vel[2] += 1 if self.pos[2] < moon.pos[2] else -1 if self.pos[2] > moon.pos[2] else 0

    def run_step(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.pos[2] += self.vel[2]

    def calculate_energy(self):
        return sum(map(lambda p: abs(p), self.pos)) * sum(map(lambda v: abs(v), self.vel))

    def x_vals(self):
        return self.pos[0], self.vel[0]

    def y_vals(self):
        return self.pos[1], self.vel[1]

    def z_vals(self):
        return self.pos[2], self.vel[2]


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


if __name__ == "__main__":
    f = open("day12.txt").read()
    moons = []
    for moon in f.split("\n"):
        moon = moon.strip('<>')
        x, y, z = moon.split(",")
        moons.append(Moon(int(x[2:]), int(y[3:]), int(z[3:])))
    for _ in range(1000):
        for moon in moons:
            moon.calculate_velocity(moons)
        for moon in moons:
            moon.run_step()

    total_energy = sum(map(lambda m: m.calculate_energy(), moons))
    print(total_energy)

    moons = []
    for moon in f.split("\n"):
        moon = moon.strip('<>')
        x, y, z = moon.split(",")
        moons.append(Moon(int(x[2:]), int(y[3:]), int(z[3:])))

    x_seen = set()
    y_seen = set()
    z_seen = set()
    steps = 0
    x_steps = -1
    y_steps = -1
    z_steps = -1
    while x_steps == -1 or y_steps == -1 or z_steps == -1:
        x_str = str(list(map(lambda m: m.x_vals(), moons)))
        y_str = str(list(map(lambda m: m.y_vals(), moons)))
        z_str = str(list(map(lambda m: m.z_vals(), moons)))
        if x_steps == -1 and x_str in x_seen:
            x_steps = steps
        if y_steps == -1 and y_str in y_seen:
            y_steps = steps
        if z_steps == -1 and z_str in z_seen:
            z_steps = steps
        x_seen.add(x_str)
        y_seen.add(y_str)
        z_seen.add(z_str)
        steps += 1
        for moon in moons:
            moon.calculate_velocity(moons)
        for moon in moons:
            moon.run_step()
    print(lcm(x_steps, lcm(z_steps, y_steps)))
