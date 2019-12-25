from abc import abstractmethod


class AbstractIntcodeIO:
    @abstractmethod
    def input(self):
        pass

    @abstractmethod
    def output(self, out):
        pass


class DefaultIntcodeIO(AbstractIntcodeIO):
    def input(self):
        return int(input("Please input a number: "))

    def output(self, out):
        print(out)


class Intcode:
    def __init__(self, prog, io):
        self.curr = 0
        self.relative_base = 0
        self.prog = prog
        self.io = io

    @staticmethod
    def calculate_modes(instruction):
        modes = []
        instruction = instruction // 100
        modes.append(instruction % 10)
        instruction = instruction // 10
        modes.append(instruction % 10)
        instruction = instruction // 10
        modes.append(instruction % 10)
        return modes

    def calculate_addresses(self, modes):
        addresses = []
        count = 1
        for mode in modes:
            if mode == 0:
                addresses.append(self.prog[self.curr + count])
            elif mode == 1:
                addresses.append(self.curr + count)
            elif mode == 2:
                addresses.append(self.relative_base + self.prog[self.curr + count])
            count += 1
        return addresses

    def run(self):
        while self.prog[self.curr] != 99:
            instruction = self.prog[self.curr]
            modes = self.calculate_modes(instruction)
            addresses = self.calculate_addresses(modes)
            if instruction % 10 == 1:
                try:
                    self.prog[addresses[2]] = self.prog[addresses[0]] + self.prog[addresses[1]]
                except:
                    return
                self.curr += 4
            elif instruction % 10 == 2:
                try:
                    self.prog[addresses[2]] = self.prog[addresses[0]] * self.prog[addresses[1]]
                except:
                    return
                self.curr += 4
            elif instruction % 10 == 3:
                self.prog[addresses[0]] = self.io.input()
                self.curr += 2
            elif instruction % 10 == 4:
                self.io.output(self.prog[addresses[0]])
                self.curr += 2
            elif instruction % 10 == 5:
                if self.prog[addresses[0]] != 0:
                    self.curr = self.prog[addresses[1]]
                else:
                    self.curr += 3
            elif instruction % 10 == 6:
                if self.prog[addresses[0]] == 0:
                    self.curr = self.prog[addresses[1]]
                else:
                    self.curr += 3
            elif instruction % 10 == 7:
                self.prog[addresses[2]] = 1 if self.prog[addresses[0]] < self.prog[addresses[1]] else 0
                self.curr += 4
            elif instruction % 10 == 8:
                self.prog[addresses[2]] = 1 if self.prog[addresses[0]] == self.prog[addresses[1]] else 0
                self.curr += 4
            elif instruction % 10 == 9:
                self.relative_base += self.prog[addresses[0]]
                self.curr += 2


def code_to_prog(code):
    return [int(x) for x in code.split(",")]
