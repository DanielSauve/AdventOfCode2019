import sys


def run(noun, verb, nums):
    curr = 0
    nums[1] = noun
    nums[2] = verb
    while nums[curr] != 99:
        if nums[curr] == 1:
            pos1 = nums[curr + 1]
            pos2 = nums[curr + 2]
            out = nums[curr + 3]
            try:
                nums[out] = nums[pos1] + nums[pos2]
            except:
                return
        elif nums[curr] == 2:
            pos1 = nums[curr + 1]
            pos2 = nums[curr + 2]
            out = nums[curr + 3]
            try:
                nums[out] = nums[pos1] * nums[pos2]
            except:
                return
        curr = curr + 4
    return nums[0]


f = open("./day2.txt")
txt = f.read().split(",")
nums = [int(x) for x in txt]
print(run(12, 2, nums))
for noun in range(100):
    for verb in range(100):
        if run(noun, verb, nums) == 19690720:
            print(100 * noun + verb)
            sys.exit()
        nums = [int(x) for x in txt]
    nums = [int(x) for x in txt]
