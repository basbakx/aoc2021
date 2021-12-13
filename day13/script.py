import numpy as np
f = open('/Users/bas/aoc2021/day13/input.txt', 'r')

x = f
ins = []
cx = []
cy = []

# Setup rules
for val in x:
    val = val.strip()
    if 'fold' in val:
        val = val.replace("fold along ","");
        c, v = val.split('=')
        ins.append([c, int(v)])
    elif val != '':
        xx, yy = val.split(',')
        cx.append(int(xx))
        cy.append(int(yy))

s = (max(cy) + 1, max(cx) + 1)
mat = np.zeros(s)

for v in range(len(cx)):
    mat[cy[v]][cx[v]] = 1


# Solve 1 and 2
first = True
for v in ins:
    if v[0] == 'y':
        mat1= np.vsplit(mat, [v[1], v[1] + 1])

        mat1[0] = np.flipud(mat1[0])
        if len(mat1[0]) > len(mat1[2]):
            big = mat1[0]
            small = mat1[2]
        else:
            big = mat1[2]
            small = mat1[0]

        for i in range(len(big)):
            if i < len(small):
                big[i] = big[i] + small[i]

        big = np.flipud(big)
        if first:
            xmat = np.array(big)
            first = False

    if v[0] == 'x':
        mat1= np.hsplit(mat, [v[1], v[1] + 1])

        mat1[0] = np.fliplr(mat1[0])
        if len(mat1[0][0]) >= len(mat1[2][0]):
            big = mat1[0]
            small = mat1[2]
        else:
            big = mat1[2]
            small = mat1[0]

        for i in range(len(small)):
            big[i] = big[i] + small[i]
        if first:
            xmat = np.array(big)
            first = False
        big = np.fliplr(big)
    mat = big

x = 0
y = 0

for val in np.nditer(xmat):
    if val != 0: x += 1

for val in np.nditer(mat):
    if val != 0: y += 1



np.set_printoptions(linewidth=np.inf)
res = np.where(mat>0, '#', mat)
res = np.where(res=='0.0', ' ', res)

print("Answer 1:", x)
print("Answer 2:")
print(res)
# CJHAZHKU