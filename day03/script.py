from collections import Counter

list = [0] * 12
list2 = []
l = 0

f = open('/Users/bas/aoc2021/day03/input.txt', 'r')
for line in f.readlines():
    l += 1
    w = [int(c) for c in line.strip()]
    templist = []
    for i,j in enumerate(w):
        list[i] += j
        templist.append(j)
    list2.append(templist)

# Solve 1
g = ''
e = ''
for i in list:
    if i < l/2:
        g += '0'
        e += '1'
    else:
        g += '1'
        e += '0'

x = int(g,2) * int(e,2)

# Solve 2
def most(val, num, switch):        
    returnval = []
    templist = []
    for i in val:
        templist.append(int(i[num]))
    data = Counter(templist)
    if data[0] > data[1]:
        com = 0 if switch else 1
    else:
        com = 1 if switch else 0

    for i in val:
        if int(i[num]) == com:
            returnval.append(i)
    return returnval

ol = list2
cl = list2

for i in range(len(ol[0])):
    if len(ol) > 1:
        ol = most(ol, i, 1)

for i in range(len(cl[0])):
    if len(cl) > 1:
        cl = most(cl, i, 0)

o = ''
c = ''
for i in ol[0]:
    o += str(i)
for i in cl[0]:
    c += str(i)

y = int(o, 2) * int(c, 2)

print("Answer 1:", x)
print("Answer 2:", y)