

# 📡 탐색 알고리즘

## 🏛️ DFS / BFS 구현을 위한 필요한 자료구조
DFS와 BFS에는 탐색 알고리즘인 만큼 탐색에 대한 기록이 필요하게 됩니다. 마치 족적을 남기는 것처럼 어느 노드(위치)를 지나왔는지에 대해서 말이죠.

그렇지만 마냥 저장만 하게 될 경우에는 데이터의 수가 큰 상황에서 메모리 Overflow가 발생하는 참사를 겪게 될 겁니다.

이를 방지하고자 `Stack` 과 `Queue` 라는 자료구조를 알아야 합니다. 이를 간단히 설명하자면 아래의 그림과 같다고 할 수 있습니다.

<p align = 'center'><img width="864" alt="Stack & Queue" src="https://user-images.githubusercontent.com/99489807/231467474-66695de2-14d4-4a03-96f9-6206dbdad623.png"></p>


## 🪛 DFS (Depth First Search)

깊이 우선 탐색이라는 이름에 맞게 Stack 자료구조를 기반으로 간단한 구현이 가능합니다. 실제로는 스택을 사용하지 않아도 되지만 말이죠.

탐색 중 시간 복잡도는 데이터의 개수가 N개인 경우 `O(N)`이 소요가 된다는 것을 알 수 있습니다.

구현 시에 각 노드가 연결된 정보는 2차원 리스트로, 각 노드가 방문된 정보는 1차원 리스트로 표현하여 함수를 호출한다는 점을 기억해두면 좋습니다. 이와 관련된 내용은 [링크](github.com/jwyeeh-dev/StudyAlgorithm)에 자세히 설명되어 있습니다.

### **아래는 DFS를 함수화하여 구현하였을 때의 소스 코드 예시입니다.**

```python
def dfs(graph, v, visted):
    # 현재 노드를 방문 처리
    # 방문 처리 (스택에 한 번 삽입되어 처리된 노드가 다시 삽입되지 않게 체크하는 것.)
    # 각 노드를 한 번씩만 처리할 수 있다는 점.
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

```

## 🏃🏻 BFS (Breadth First Search)


### **아래는 BFS를 함수화하여 구현하였을 때의 소스 코드 예시입니다.**

```python
from collections import deque

def bfs(graph, start, visited):
    # Queue 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # queue가 비워질 때까지 반복
    while queue:
        # queue에서 하나의 원소를 뽑아 출력함.
        v = queue.popleft()
        print(v, end = ' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 queue에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
```