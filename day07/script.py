import numpy as np
f = open('/Users/bas/aoc2021/day07/input.txt', 'r')


# Crabpos
for i in f: crabPos = list(map(int, i.split(',')))


# Solve part 1
medianPos = int(np.median(crabPos))
x = 0
for i in crabPos: x += abs(medianPos - i)


# Solve part 2
meanPos = int(np.average(crabPos))
print(meanPos)
y = 0
for i in crabPos:
    dif = abs(i - meanPos)
    y += int(((dif**2)+dif)/(2))


print("Answer 1:", x)
print("Answer 2:", y)
