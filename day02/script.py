x = 0
y = 0
l = []
aim = 0
pos = 0

d = {'forward': 0, 'up': 0, 'down': 0}
f = open('/Users/bas/aoc2021/day02/input.txt', 'r')
for line in f.readlines():
    name,score = line.split()
    s = int(score)
    l.append([name,s])
    d[name] += int(s)
    if name == 'down':
        aim += s
    elif name == 'up':
        aim -= s
    elif name == 'forward':
        pos += aim * s

x = d['forward'] * (d['down'] - d['up'])
y = d['forward'] * pos

print("Answer 1:", x)
print("Answer 2:", y)