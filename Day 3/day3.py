import sys

f = open("./day3.txt")
[first, second] = f.readlines()
traveled = dict()
curr_x, curr_y = 0, 0
count = 0
for item in first.split(","):
    direction = item[0]
    if direction == "R":
        amount = int(item[1:])
        for x in range(amount):
            curr_x += 1
            count += 1
            pos = str(curr_x) + "," + str(curr_y)
            if pos not in traveled:
                traveled[pos] = count
    elif direction == "L":
        amount = int(item[1:])
        for x in range(amount):
            curr_x -= 1
            count += 1
            pos = str(curr_x) + "," + str(curr_y)
            if pos not in traveled:
                traveled[pos] = count
    elif direction == "U":
        amount = int(item[1:])
        for y in range(amount):
            curr_y -= 1
            count += 1
            pos = str(curr_x) + "," + str(curr_y)
            if pos not in traveled:
                traveled[pos] = count
    elif direction == "D":
        amount = int(item[1:])
        for y in range(amount):
            curr_y += 1
            count += 1
            pos = str(curr_x) + "," + str(curr_y)
            if pos not in traveled:
                traveled[pos] = count
distance = sys.maxsize
latency = sys.maxsize
curr_x, curr_y = 0, 0
count = 0
for item in second.split(","):
    direction = item[0]
    if direction == "R":
        amount = int(item[1:])
        for x in range(amount):
            curr_x += 1
            count += 1
            pos = str(curr_x) + "," + str(curr_y)
            dis = abs(curr_x) + abs(curr_y)
            if pos in traveled:
                distance = min(distance, dis)
                latency = min(count + traveled[pos], latency)
    elif direction == "L":
        amount = int(item[1:])
        for x in range(amount):
            curr_x -= 1
            count += 1
            pos = str(curr_x) + "," + str(curr_y)
            dis = abs(curr_x) + abs(curr_y)
            if pos in traveled:
                distance = min(distance, dis)
                latency = min(count + traveled[pos], latency)
    elif direction == "U":
        amount = int(item[1:])
        for y in range(amount):
            curr_y -= 1
            count += 1
            pos = str(curr_x) + "," + str(curr_y)
            dis = abs(curr_x) + abs(curr_y)
            if pos in traveled:
                distance = min(distance, dis)
                latency = min(count + traveled[pos], latency)
    elif direction == "D":
        amount = int(item[1:])
        for y in range(amount):
            curr_y += 1
            count += 1
            pos = str(curr_x) + "," + str(curr_y)
            dis = abs(curr_x) + abs(curr_y)
            if pos in traveled:
                distance = min(distance, dis)
                latency = min(count + traveled[pos], latency)
print(distance)
print(latency)
