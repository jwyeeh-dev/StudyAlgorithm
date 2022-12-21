from collections import Counter

N = int(input())
dirs = Counter()
dirs = str(input().split())

loc = [1,0]

for dir in dirs:
    if loc[0] == 0 and loc[1] == 0:
        if dir == 'R':
            loc[0] += 1
        elif dir == 'D':
            loc[1] -= 1 
        else:
            continue

    elif loc[0] != 0 and loc[1] != 0:
        if dir == 'R':
            loc[0] += 1
        elif dir == 'L':
            loc[0] -= 1
        elif dir == 'U':
            loc[1] += 1
        elif dir == 'D':
            loc[1] -= 1
    
    elif loc[0] == 0:
        if dir == 'R'

print(loc)



