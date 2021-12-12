import numpy as np

f = open('/Users/bas/aoc2021/day11/input.txt', 'r')
l = []
for val in f: l.append(list(val.strip()))

n = np.matrix(l).astype(int)


# Border increases function
v = [[-1, -1], [-1,0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0,-1]]
def bord(loc, ma):
    for i in v:
        yv = loc[0] + i[0]
        xv = loc[1] + i[1]
        if yv < n.shape[0] and yv >= 0 and xv < n.shape[1] and xv >= 0:
            n[loc[0] + i[0], loc[1] + i[1]] += 1


# Flash check function
done = []
xt = 0
def check(ma):
    global done
    global xt
    c = 0
    co = np.where(n > 9)
    co = list(zip(co[0], co[1]))
    for i in co:
        if i not in done:
            c += 1
            xt += 1
            done.append(i)
            bord(i, n)
    if c > 0:
        check(n)
    else:
        for i in done:
            n[i] = 0


# Solve 1 and 2
x = 0
y = 0
res = 0
step = 0
while res != n.shape[0] * n.shape[1]:
    n += 1
    res = len(done)
    y = step
    if step == 100: x = xt
    
    for (j,k), value in np.ndenumerate(n):
        if n[j, k] >= 100:
            n[j, k] = 0
    
    done = []
    check(n)

    step += 1

    # Debug
    # print('')
    # print('STEP', step, res)
    # print(n)

print("Answer 1:", x)
print("Answer 2:", y)
