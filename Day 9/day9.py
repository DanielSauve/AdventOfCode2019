from intcode import Intcode, code_to_prog, DefaultIntcodeIO

if __name__ == "__main__":
    f = open("day9.txt").read()
    prog = code_to_prog(f)
    prog.extend([0 for _ in range(10000)])
    i = Intcode(prog, DefaultIntcodeIO())
    i.run()
