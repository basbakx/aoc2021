f = open('/Users/bas/aoc2021/day05/input.txt', 'r')


# Create coordinates
lines = []
for i, val in enumerate(f):
    x,z,y = val.split()
    x1, y1 = x.split(',')
    x2, y2 = y.split(',')
    lines.append([[int(x1),int(y1)],[int(x2),int(y2)]])


# Solve part 1 and 2 matrixes
x = 0
y = 0

vals1 = [[0]*1000 for i in range(1000)]
vals2 = [[0]*1000 for i in range(1000)]

for line in lines:
    x1 = line[0][0]
    x2 = line[1][0]
    y1 = line[0][1]
    y2 = line[1][1]

    yh = max(y1, y2)
    yl = min(y1, y2)
    xh = max(x1, x2)
    xl = min(x1, x2)

    xr = abs(xh - xl)
    yr = abs(yh - yl)

    if y1 == y2:
        for m in range(0 , xr+1):
            vals1[y1][xl+m] += 1
            vals2[y1][xl+m] += 1
    elif x1 == x2:
        for m in range(0, yr+1):
            vals1[yl+m][x1] += 1
            vals2[yl+m][x1] += 1
    else:
        xr = list(range(xl,xh + 1))
        if x1 > x2:
            xr.reverse()
        yr = list(range(yl,yh + 1))
        if y1 > y2:
            yr.reverse()
        for m in range(len(yr)):
            vals2[yr[m]][xr[m]] += 1


# Count overlaps
for i in vals1:
    for j in i:
        if j > 1:
            x += 1

for i in vals2:
    for j in i:
        if j > 1:
            y += 1


print("Answer 1:", x)
print("Answer 2:", y)