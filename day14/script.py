f = open('/Users/bas/aoc2021/day14/input.txt', 'r')

# Process input into dictionary of rules and list of pairs
d = {}
p = []

for val in f:
    val = val.strip()
    if '->' in val:
        c, v = val.split(' -> ')
        d[c] = v
    elif val != '':
        p = list(val)


# Create dictionary of initial letter pairs
pairs = {}

for i in range(len(p) - 1):
    pair = p[i] + p[i + 1]
    if pair in pairs: 
        pairs[pair] += 1
    else: 
        pairs[pair] = 1
pairs[p[-1]] = 1


# Create stepping function
def step(pairs):
    nPairs = {}

    def add(val, count):
        if val in nPairs: 
            nPairs[val] += count
        else: 
            nPairs[val] = count

    for v in pairs:
        count = pairs[v]
        if v in d:
            add(v[0] + d[v], count)
            add(d[v] + v[1], count)
        else:
            add(v, count)

    return nPairs


# Solve function
def solve():
    res = {}

    for val in pairs:
        if val[0] in res: 
            res[val[0]] += pairs[val]
        else: 
            sres[val[0]] = pairs[val]

    res = res.values()
    return max(res) - min(res)


# Solve 1
for i in range(10): pairs = step(pairs)
x = solve()


# Solve 2
for i in range(30): pairs = step(pairs)
y = solve()


print("Answer 1:", x)
print("Answer 2:", y)