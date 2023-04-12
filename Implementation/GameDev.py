'''
[고려해야 할 상황]
0. 방문한 칸 카운트
1. 왼쪽 회전 동작 구현
2. 가보지 않은 칸이면, 왼쪽 회전 후 1칸 전진
3. 가본 칸이면 왼쪽 회전 후 1단계
4. 네 방향 모두 이미 가본 칸 또는 바다 칸이면 1칸 후진 -> 뒤쪽 방향이 바다인 칸 : 종료
'''

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

# 위치 표시용 지도
d = [[0] * m for _ in range(n)]

# 족적 확인
d[x][y] = 1

# 전체 지형 정보 저장
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

# 왼쪽 회전 동작
def turn_left():
    global direction
    direction -= 1

    if direction == -1:
        direction = 3

# 이동 카운트 및 회전 시간 카운트
count = 1
turn_time = 0

# 북, 동, 남, 서 이동 방향
dx = [-1,0,1,0]
dy = [0,1,0,-1]

while True:
    #왼쪽으로 회전하고 갈 곳을 탐색하는 과정
    turn_left()
    # 회전 후 정면에 대하여 왼쪽으로 이동하는 좌표 예측 저장
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 아직 가지 않았고, 육지라면 왼쪽으로 전진 -> 예측된 좌표를 현재 좌표로 갱신
    if d[nx][ny] == 0 and maps[nx][ny] == 0:
        d[nx][ny] = 1
        # 전진
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    # 가본 칸이고, 육지인 경우 왼쪽으로 다시 돌림.
    else:
        turn_time += 1

    # 네 방향 모두 이미 가본 칸이거나 바다인 경우, 방향 그대로 1칸 후진 
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        # 육지일 경우, 후진
        if d[nx][ny] == 0:
            x = nx
            y = ny

        # 바다인 경우
        else:
            break
        turn_time = 0

print(count)