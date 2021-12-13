from itertools import chain
f = open('/Users/bas/aoc2021/day12/input.txt', 'r')


# Create mapping
map = {}
for val in f:
    val = val.strip()
    val = val.split('-')
    if val[0] in map:
        if val[1] not in map[val[0]]:
            map[val[0]].append(val[1])
    else:
        map[val[0]] = []
        map[val[0]].append(val[1])
    if val[1] in map:
        if val[0] not in map[val[1]]:
            map[val[1]].append(val[0])
    else:
        map[val[1]] = []
        map[val[1]].append(val[0])


# Initial map step
res = [['start']]


# Mapping function
x = 0
y = 0

def run(list):
    global x
    global y
    res2 = []
    for path in list:
        if path[-1] == 'end':
            print('n')
        elif path[-1] in map:
            for opt in map[path[-1]]:
                if opt == 'end':
                    y += 1
                    if path[0] == 'start':
                        x += 1
                elif opt.isupper():
                    res2.append(path + [opt])
                elif opt not in path and opt != 'start':
                    res2.append(path + [opt])
                elif opt != 'start' and path[0] == 'start':
                    res2.append(['d']+path+ [opt])
    return res2

# Solve 1 and 2
while len(res) > 0:
    res = run(res)


print("Answer 1:", x)
print("Answer 2:", y)