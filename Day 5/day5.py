from intcode import Intcode, code_to_prog

if __name__ == "__main__":
    f = open("day5.txt").read()
    prog = code_to_prog(f)
    intcode = Intcode(prog)
    intcode.run()
