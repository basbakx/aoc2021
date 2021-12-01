x = 0
y = 0
window = 0
lastWindow = 0

with open('/Users/bas/AoC/day1/input.txt') as file:
    lines = [int(x) for x in file.read().split()]

for i, val in enumerate(lines):
    if val > lines[i-1]:
        x += 1

for i, val in enumerate(lines):
    if i < ( len(lines) - 2 ):
        window = (lines[i] + lines[i+1] + lines[i+2])
        if i > 0:
            if window > lastWindow:
                y += 1
            lastWindow = window

print("Answer 1:", x)
print("Answer 2:", y)