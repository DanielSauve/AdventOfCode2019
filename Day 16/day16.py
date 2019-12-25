def gen_pattern(n, memo):
    if n not in memo:
        base_pattern = [0, 1, 0, -1]
        out = []
        for item in base_pattern:
            for _ in range(n):
                out.append(item)
        memo[n] = out
    return memo[n]


if __name__ == "__main__":
    f = open("day16.txt").read()
    curr_num = [int(x) for x in f]
    memo = dict()
    memo[0] = [0, 1, 0, -1]
    for _ in range(100):
        next_num = []
        for i in range(len(curr_num)):
            pattern = gen_pattern(i + 1, memo)
            num = 0
            curr_pat = 1
            for item in curr_num:
                num += item * pattern[curr_pat]
                curr_pat = (curr_pat + 1) % len(pattern)
            next_num.append(abs(num) % 10)
        curr_num = next_num
    print("".join(map(lambda x: str(x), curr_num[:8])))
