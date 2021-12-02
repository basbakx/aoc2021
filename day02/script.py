x = 0
y = 0
l = []
aim = 0
pos = 0

d = {'forward': 0, 'up': 0, 'down': 0}
f = open('/Users/bas/aoc2021/day02/input.txt', 'r')
for line in f.readlines():
    n,v = line.split()
    v = int(v)
    l.append([n,v])
    d[n] += int(v)
    if n == 'down':
        aim += v
    elif n == 'up':
        aim -= v
    elif n == 'forward':
        pos += aim * v

x = d['forward'] * (d['down'] - d['up'])
y = d['forward'] * pos

print("Answer 1:", x)
print("Answer 2:", y)