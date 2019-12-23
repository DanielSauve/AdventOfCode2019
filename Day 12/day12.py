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
