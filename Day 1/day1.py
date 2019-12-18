modules = open("./day1.txt").read()
total1 = 0
total2 = 0
for module in modules.split():
    weight = int(module)
    total1 = total1 + (weight // 3) - 2
    while weight > 0:
        weight = weight // 3 - 2
        total2 = total2 if weight <= 0 else total2 + weight
print(total1)
print(total2)
