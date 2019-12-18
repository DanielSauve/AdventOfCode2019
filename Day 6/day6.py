f = open("day6.txt")
orbits = dict()
transfers = dict()
for line in f.readlines():
    line = line.strip("\n")
    first, second = line.split(")")
    orbits[second] = first
    if first in transfers:
        transfers[first].append(second)
    else:
        transfers[first] = [second]
    if second in transfers:
        transfers[second].append(first)
    else:
        transfers[second] = [first]
count = 0
for planet in orbits.keys():
    while orbits[planet] in orbits:
        count += 1
        planet = orbits[planet]
    count += 1
print(count)
curr = "YOU"
dest = "SAN"
dist = 0
possibilities = [(item, 1) for item in transfers[curr]]
seen = set(curr)
while curr != dest:
    curr, dist = possibilities.pop(0)
    seen.add(curr)
    for item in transfers[curr]:
        if item not in seen:
            possibilities.append((item, dist + 1))
print(dist - 2)
