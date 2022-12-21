def dfs(x, y):
    global apt_num

    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if area[x][y] == 1:
        area[x][y] = 0
        apt_num += 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True

    return False

n = int(input())

area = []
for i in range(n):
    area.append(list(map(int, input())))

cnt_apt = 0
apt_num = 0
apt_list = []

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            cnt_apt += 1
            apt_list.append(apt_num)
            apt_num = 0
# 오름차순 정렬 인지.
apt_list = sorted(apt_list)
 
print(cnt_apt)
for i in range(len(apt_list)):
    print(apt_list[i])

