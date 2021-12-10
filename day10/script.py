f = open('/Users/bas/aoc2021/day10/input.txt', 'r')

l = []
for val in f: l.append(list(val))


# Check lines
op = ('<', '{', '[', '(')
cl = ('>', '}', ']', ')')
err = []
inc = []

for i in l:
    cur = []
    for c, j in enumerate(i):
        if j in op:
            cur.append(j)
        elif j in cl:
            if cl.index(j) == op.index(cur[-1]):
                cur.pop()
            else:
                err.append(j)
                cur = []
                break
    if len(cur) > 0:
        inc.append(list(cur))


# Solve 1
x = 0
for i in err:
    if i == ')': x += 3
    if i == ']': x += 57
    if i == '}': x += 1197
    if i == '>': x += 25137


# Solve 2
yl = []
for i in inc:
    i.reverse()
    s = 0
    for j in i:
        s *= 5
        if j == '(': s += 1
        if j == '[': s += 2
        if j == '{': s += 3
        if j == '<': s += 4
    yl.append(s)

yl = sorted(yl)
y = yl[int((len(yl) - 1)/2)]


print("Answer 1:", x)
print("Answer 2:", y)