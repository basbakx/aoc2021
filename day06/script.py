f = open('/Users/bas/aoc2021/day06/input.txt', 'r')


# Define dictionary
dict = dict.fromkeys(range(10), 0)

for i, val in enumerate(f):
    fish = val.split(',')
    for i in range(len(fish)):
        dict[int(fish[i])] += 1


# Create fishy function
def day(f):
    if f[0] > 0:
        f[7] += f[0]
        f[9] = f[0]
    for i in range(1, len(dict)):
        f[i - 1] = f[i]
    f[9] = 0
    return f

def count():
    c = 0
    for i in range(len(dict)): c += dict[i]
    return c
    

# Solve part 1
x = 0
for i in range(80):  dict = day(dict)
for i in range(len(dict)): x += dict[i]


# Solve part 2
y = 0
for i in range(80, 256): dict = day(dict)
for i in range(len(dict)): y += dict[i]


print("Answer 1:", x)
print("Answer 2:", y)
