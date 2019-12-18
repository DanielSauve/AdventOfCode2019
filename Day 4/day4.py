import re

puzzle = "109165-576723"
start, end = puzzle.split("-")
match1 = re.compile(r"(\d)\1")
match2 = re.compile(r"^1*2*3*4*5*6*7*8*9*$")
match3 = re.compile(
    r"^(1{2}[^1]+|[^2]*2{2}[^2]*|[^3]*3{2}[^3]*|[^4]*4{2}[^4]*|[^5]*5{2}[^5]*|[^6]*6{2}[^6]*|[^7]*7{2}[^7]*|[^8]*8{2}"
    r"[^8]*|[^9]+9{2})$")
count1 = 0
count2 = 0
for i in range(int(start), int(end) + 1):
    s = str(i)
    if re.search(match1, s) and re.search(match2, s):
        count1 += 1
        if re.search(match3, s):
            count2 += 1
print(count1)
print(count2)
