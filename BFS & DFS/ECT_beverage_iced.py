
def dfs(x, y):
    #범위를 벗어나면 종료하도록 함.
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    # 얼음 칸 퍼지게
    if mold[x][y] == 0:
        mold[x][y] = 1
        # 재귀함수 사용
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True

    # 재귀함수 완료되면 종료.
    return False
     

n, m = map(int, input().split())

mold = []
for i in range(n):
    mold.append(list(map(int, input())))

cnt = 0
for i in range(n):
    for j in range(m):
        # 각각의 위치에 대하여 DFS 수행
        if dfs(i, j) == True:
            cnt += 1
            print("cnt : %d" % cnt)
            print("location : (%d, %d)" % (i, j))

# 결과값 출력
print(cnt)




