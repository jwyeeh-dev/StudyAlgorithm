'''
[순서]
1. 한 지점의 상, 하, 좌, 우를 확인하여 '0' and 방문하지 않은 지점이 있다면 방문처리
2. 반복 (재귀함수 활용하는 DFS 활용)
3. 모든 노드에 반복하며 방문하지 않은 지점 카운트
4. 틀의 크기를 벗어날 경우 함수 종료 (재귀함수로 DFS 함수를 구성할 것이기 때문.)
'''

n, m =  map(int, input().split())

maps = []
# 얼음 틀의 모양
for i in range(n):
    maps.append(list(map(int, input())))

def dfs(x, y):
    # 범위를 벗어날 경우에 대한 종료 조건 주입
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 칸을 방문하지 않았다고 판단 시
    if maps[x][y] == 0:
        # 현재 칸에 대한 방문 처리 진행.
        maps[x][y] = 1
        
        # 상, 하, 좌, 우 칸에 대하여 재귀 반복
        dfs(x, y+1)
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y-1)

        # 음료수 칸 안에서 재귀 반복이 제대로 동작 중임을 표시
        return True
    # 재귀 반복이 안된다면 음료수 칸을 벗어났다고 판단.
    return False

# 모든 칸에 대하여 음료수를 채우는 작업
count = 0
for i in range(n):
    for j in range(m):
        # 현재 칸에 대하여 DFS 수행
        if dfs(i, j) == True:
            count += 1

print(count)