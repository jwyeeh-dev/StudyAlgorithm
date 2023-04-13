# 미로 탈출

- 난이도: 1.5
- 메모리 제한: 128MB
- 문제 유형: DFS/BFS
- 시간 제한: 1초
- 풀이 시간: 30분

### 문제 내용


### 1차 시도 [실패]

**실행 결과**
- 최소 칸의 개수가 아닌 1이 있는 모든 칸의 개수를 세는 결과가 나오는 것으로 보입니다.
- DFS로 해결하려고 하였는데 그로 인하여 조건을 충족하지 못하였다고 예상하였습니다.

---

**코드**

```python
n, m = map(int, input().split())

maps = []
for i in range(n):
    maps.append(list(map(int, input())))

def dfs(x, y):
    global count
    # 종료 조건
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if maps[x][y] == 1:
        maps[x][y] = 0

        dfs(x, y+1)
        dfs(x+1, y)
        
        count += 1

        return True
    
    return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            dfs(i,j)

print(count)
```

---

**문제점**

1. 기존 코드는 count를 누적하여 총 1의 개수를 계산하려고 시도합니다. 하지만 이 방법은 최소 이동 칸의 개수를 찾는 문제와는 관련이 없습니다.
2. 종료 조건에서 x, y의 범위를 검사하는 것은 좋습니다. 하지만, 이 경우에도 최소 이동 칸의 개수와는 관련이 없습니다.
3. 종료 조건은 (n-1, m-1) 위치에 도달했을 때 설정해야 합니다. 그러나 현재 코드는 이를 고려하지 않고 있습니다.

---

### 2차 시도 [실패]

**실행 결과**
- 칸의 개수 카운트가 제대로 되고 있지 않았습니다.
- DFS로 해결하려고 하였는데 그로 인하여 조건을 충족하지 못하였다고 예상하였습니다.

---

**코드**

```python
n, m = map(int, input().split())

maps = []
for i in range(n):
    maps.append(list(map(int, input())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        

        if x <= -1 or x >= n or y <= -1 or y >= m:
            return False
    
        if maps[nx][ny] == 0:
            continue

        if maps[nx][ny] == 1:
            maps[nx][ny] = maps[x][y] + 1
            x = nx
            y = ny
            

    return maps[n-1][m-1]

print(dfs(0,0))
```

---

**문제점**

1. **`dfs`** 함수를 **`bfs`**로 변경했습니다. DFS(깊이 우선 탐색) 대신 BFS(너비 우선 탐색)를 사용해 최소 이동 칸의 개수를 구할 수 있습니다. DFS는 스택을 사용하지만, BFS는 큐를 사용합니다. 여기서는 **`deque`**를 사용하여 큐를 구현했습니다.
2. 기존 **`dfs`** 함수에서는 이동 경로를 체크하지 않고 바로 반환했습니다. 이것을 수정하여, 큐가 비어있지 않을 때까지 반복문을 수행하도록 했습니다.
3. 기존 코드에서는 이동할 때마다 x와 y를 변경했습니다. 하지만, 이렇게 하면 다른 방향으로 이동할 때 문제가 발생합니다. 수정된 코드에서는 nx와 ny를 사용하여 다음 위치를 계산하고, 조건에 맞으면 큐에 추가합니다.

---

### 최종 코드 [성공]

1. **BFS를 이용한 코드**
    - BFS의 구조 특성을 이용하는 것이 좋아 보입니다.
    - BFS는 Queue를 활용하여 최소 이동 칸의 개수를 구할 수 있다는 장점이 있습니다.
    
    ```python
    from collections import deque
    
    n, m = map(int, input().split())
    
    maps = []
    for i in range(n):
        maps.append(list(map(int, input())))
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        
        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                    
                if maps[nx][ny] == 0:
                    continue
                    
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
                    
        return maps[n-1][m-1]
    
    print(bfs(0, 0))
    ```
    

1. **그렇다면 DFS로는 할 수 없을까?**
    - `**할 수 있습니다.**`
    - 예시 코드는 아래와 같습니다.
        1. count 변수를 추가하여 이동 칸의 개수를 기록합니다.
        2. DFS의 기본 구조를 변경하여 현재 위치에서 상하좌우로 이동하면서 최소 이동 칸의 개수를 찾습니다.
        3. 종료 조건을 변경하여 (n-1, m-1) 위치에 도달했을 때 count를 반환하도록 합니다.
        4. 벽을 만나거나 이동할 수 없는 경우, float('inf')를 반환하여 최소 이동 칸의 개수를 찾을 수 없음을 나타냅니다.
        5. 함수 호출을 반복문에서 제거하고, dfs 함수 내부에서 재귀 호출을 수행합니다.
        6. 이동 후에 다시 돌아오기 위해, maps[x][y] 값을 1로 복원합니다.
    
    ```python
    n, m = map(int, input().split())
    
    maps = []
    for i in range(n):
        maps.append(list(map(int, input())))
    
    def dfs(x, y, count):
        if x == n-1 and y == m-1:
            return count
        
        if x < 0 or x >= n or y < 0 or y >= m:
            return float('inf')
        
        if maps[x][y] == 0:
            return float('inf')
        
        maps[x][y] = 0
        count += 1
        
        min_count = float('inf')
        min_count = min(min_count, dfs(x+1, y, count))
        min_count = min(min_count, dfs(x-1, y, count))
        min_count = min(min_count, dfs(x, y+1, count))
        min_count = min(min_count, dfs(x, y-1, count))
        
        maps[x][y] = 1
        
        return min_count
    
    print(dfs(0, 0, 1))
    ```
    
    - **하지만 코드를 보다시피 `문제를 해결할 때 상당한 시간이 소요될 수 있고 메모리 사용량이 높아질 수 있는 치명적인 단점`이 있어 데이터의 사이즈가 커질 경우 메모리 및 소요시간 조건을 충족하지 못할 가능성이 높게 됩니다.**
    - 또한, False를 사용하여 비교할 수 없습니다. 그 이유는 아래와 같습니다.
        1. **`float('inf')`**는 이동 칸의 개수를 비교할 때 사용되는 최소 이동 칸의 개수의 초기값입니다. **`float('inf')`**는 무한대를 의미하므로, 이동 칸의 개수는 항상 더 작은 값으로 갱신됩니다. 만약 이 값을 **`False`**로 변경하면, 이동 칸의 개수와 비교할 수 없게 됩니다.
        2. **`False`**는 불리언(boolean) 타입으로, 이동 칸의 개수를 나타내는 정수와 비교할 수 없습니다. 이 코드에서는 최소 이동 칸의 개수를 찾기 위해 **`min()`** 함수를 사용합니다. **`min()`** 함수에 **`False`**와 정수를 함께 전달하면, 파이썬은 다른 타입의 객체를 비교할 수 없어 오류를 발생시킬 수 있습니다.
