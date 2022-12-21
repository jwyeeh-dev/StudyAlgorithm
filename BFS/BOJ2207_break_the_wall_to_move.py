from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, c):
    # c는 벽 파괴를 사용했는지 카운트하는 척도.
    queue = deque()
    queue.append((x,y,c))

    while queue:
        x, y, c = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][c]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우 무시함.
            if nx <= -1 or ny <= -1 or nx >= n or ny >= m:
                continue

            # 벽인 경우, 벽 파괴 안 쓴 경우, 
            if maze[nx][ny] == 1 and c == 0:
               visited[nx][ny][1] = visited[x][y][0] + 1
               queue.append((nx, ny, 1))

            # 해당 노드를 처음 방문하는 경우(visited)에만 최단 거리 기록
            elif maze[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[x][y][c] + 1
                queue.append((nx, ny, c))
            
    return(-1)


n, m = map(int, input().split())

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

maze = []
for i in range(n):
    maze.append(list(map(int, input())))


print(bfs(0,0,0))

