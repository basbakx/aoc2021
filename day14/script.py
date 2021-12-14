import re
f = open('/Users/bas/aoc2021/day14/input.txt', 'r')

d = {}
p = ''

# Setup rules
for val in f:
    val = val.strip()
    if '->' in val:
        c, v = val.split(' -> ')
        d[c] = v
    elif val != '':
        p = val

# largeString = "Lorem ipsum ###### some previous text to be erased ###### dolor sit amet"
# smallString = "foo bar"
# find = '######'
# print(re.sub(rf'{find}', smallString, largeString))

# def run(st):
#     res = ''
#     for key in d:
#         r = ''
#         re.sub(rf'{key}', key + d[key], r)
#         res += r
#     return res
        

# for i in range(1):
#     p = run(p)
    

def run(st):
    li = list(st)
    re = ''
    for i in range(len(li) - 1):
        pair = li[i] + li[i+1]
        if pair in d:
            re += li[i] + d[pair]
        else:
            re += li[i]
    re += li[-1]
    return re

for i in range(40):
    p = run(p)
    print(i)

print(len(p))
print(set(p))

xr = []
for val in set(p):
    xr.append(p.count(val))
print(max(xr) - min(xr))