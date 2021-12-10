f = open('/Users/bas/aoc2021/day10/input.txt', 'r')

l = []
for val in f: l.append(list(val))


# Check lines
op = ('(', '[', '{', '<')
cl = (')', ']', '}', '>')
err = []
inc = []

for i in l:
    cur = []
    for j in i:
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
xs = [3, 57, 1197, 25137]
for i in err: x += xs[cl.index(i)]


# Solve 2
yl = []
for i in inc:
    i.reverse()
    s = 0
    for j in i: s = s * 5 + op.index(j) + 1
    yl.append(s)

yl = sorted(yl)
y = yl[int((len(yl) - 1)/2)]


print("Answer 1:", x)
print("Answer 2:", y)