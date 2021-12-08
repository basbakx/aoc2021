f = open('/Users/bas/aoc2021/day08/input.txt', 'r')

pat = []
out = []
for i, val in enumerate(f):
    p, o = val.split(' | ')
    p = p.strip()
    o = o.strip()
    p = p.split()
    o = o.split()
    pat.append(p)
    out.append(o)


# Solve part 1 and 2
uni = [2,4,3,7]
x = 0
y = 0

for i in range(len(pat)):
    de = [''] * 10
    o = ''

    for code in pat[i]:
        l = len(code)
        if l == 2: de[1] = list(code)
        elif l == 4: de[4] = list(code)
        elif l == 3: de[7] = list(code)
        elif l == 7: de[8] = list(code)

    for code in out[i]:
        com = lambda b: len(set(code).intersection(b))
        l = len(code)
        if len(code) in uni:
            x += 1
        if l == 2: o += '1'
        elif l == 4: o += '4'
        elif l == 3: o += '7'
        elif l == 7: o += '8'
        if l == 5:
            if com(de[1]) == 2: o += '3'
            elif com(de[4]) == 2: o += '2'
            else: o += '5'
        if l == 6:
            if com(de[4]) == 4: o += '9'
            elif com(de[1]) == 2: o+= '0'
            else: o += '6'

    y += int(o)


print("Answer 1:", x)
print("Answer 2:", y)