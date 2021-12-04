f = open('/Users/bas/aoc2021/day04/input.txt', 'r')
c = 0

# Create cards and numbers
nums = []
cards = []
for i, val in enumerate(f):
    if i == 0:
        nums = val.split(',')
    elif val == '\n':
        if (i > 1):
            c += 1
        cards.append([])
    else:
        alist = val.split()
        amap = map(int, alist)
        cards[c].append(list(amap))
        

 
# Bingo check function
def check(list):
    for card in cards:
        for i in card:
            result = all(elem in list for elem in i)
            if result: 
                return (card)
        for i in range(len(card[0])):
            column = []
            for row in card:
                column.append(row[i])
            result = all(elem in list for elem in column)
            if result: 
                return (card)
    return False


# Solve 1
x = 0
numlist = []
for i in nums:
    numlist.append(int(i))
    result = check(numlist)
    if result:
        for j in result:
            for k in j:
                if k not in numlist:
                    x+=k
        x = x * numlist[-1]
        break

# Solve 2
y = 0
def recur(numlist):
    result = check(numlist)
    if result in cards:
        cards.remove(result)
        recur(numlist)

numlist2 = []
for i in nums:
    numlist2.append(int(i))
    result = check(numlist2)
    if result:
        if len(cards) > 1:
            recur(numlist2)
        else:
            for j in cards[0]:
                for k in j:
                    if k not in numlist2:
                        y+=k
            y = y * numlist2[-1]
            break

print("Answer 1:", x)
print("Answer 2:", y)