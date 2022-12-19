
bags = [5, 3]
cnt = 0
weight = int(input())

while weight >= 0:
    if weight % bags[0] == 0:
        cnt += weight // 5
        print(cnt)
        break
    weight -= bags[1]
    cnt += 1
else:
    print(-1)


