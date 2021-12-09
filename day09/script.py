f = open('/Users/bas/aoc2021/day09/input.txt', 'r')

hm = []
for val in f:
    val = val.strip()
    val = list(str(val))
    val = [int(item) for item in val]
    hm.append(val)


# Solve part 1
x = 0
bs = []
for i in range(len(hm)):
    for j in range(len(hm[i])):
        lar = lambda x, y:hm[i][j] <  hm[i + y][j + x] if j + x in range(len(hm[0])) and i + y in range(len(hm)) else 10
        if lar(0,-1) and lar(0,1) and lar(-1,0) and lar(1, 0):
            x += 1 + hm[i][j]
            bs.append([i,j])


# Solve part 2
# Retrieve height function
def hei(y,x,j):
    if (
        j[1] + x in range(len(hm[0])) and 
        j[0] + y in range(len(hm))
    ): 
        r = hm[j[0] + y][j[1] + x] 
        if r != 9:
            return hm[j[0] + y][j[1] + x] 
        else:
            return 100
    else:
        return 100

# Adjacent coördinates
tries = [[-1,0],[0,1],[1,0],[0,-1]]

#Recursion
rl = []    
def search():
    global rl
    global hm
    a = 0
    newList = []
    for j in rl:
        if j not in newList:
            newList.append(j)
        for k in tries:
            r = hei(k[0], k[1], j)
            if r in range(0,9) and [j[0] + k[0], j[1] + k[1]] not in newList:
                newList.append([j[0] + k[0], j[1] + k[1]])            

    if len(newList) > len(rl):
        rl = newList
        search()

# Calculate answer starting with all low points
basins = []
for i in range(len(bs)):
    rl = [bs[i]]
    search()
    basins.append(len(rl))

basins = sorted(basins, reverse = True)[:3]

y = 1
for i in basins: 
    y *= i


print("Answer 1:", x)
print("Answer 2:", y)