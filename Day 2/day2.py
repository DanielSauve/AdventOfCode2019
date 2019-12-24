from intcode import Intcode, code_to_prog

if __name__ == "__main__":
    f = open("day2.txt").read()
    prog = code_to_prog(f)
    prog[1], prog[2] = 12, 2
    intcode = Intcode(prog)
    intcode.run()
    print(intcode.prog[0])
    for noun in range(100):
        for verb in range(100):
            prog = code_to_prog(f)
            prog[1], prog[2] = noun, verb
            intcode = Intcode(prog)
            intcode.run()
            if intcode.prog[0] == 19690720:
                print(100 * noun + verb)
