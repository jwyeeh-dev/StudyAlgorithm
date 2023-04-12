n = int(input())

move = list(map(str, input().split()))

coor = [1,1]

for i in range(len(move)):
    if (coor[0] == 1 and move[i] == 'U') or (coor[1] == n and move[i] == 'D') or (coor[0] == 1 and move[i] == 'L') or (coor[1] == n and move[i] == 'R'):
        continue

    else:
        if move[i] == 'R':
            coor[1] += 1
        
        if move[i] == 'L':
            coor[1] -= 1

        if move[i] == 'U':
            coor[0] -= 1

        if move[i] == 'D':
            coor[0] += 1
     

print(coor[0], coor[1])