'''
개수가 10억 개를 넘어가므로 공간복잡도와 시간 복잡도를 고려해야 할 필요성이 있다.
'''

n, m = map(int, input().split())
length = map(int, input().split())

ddeok = [0 for _ in range(n)]

result = 0

start = 0
end = max(length)

while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in length:
        if x > mid:
            total += x - mid
    
    if total < m:
        end = mid - 1
    
    else:
        result = mid
        start = mid + 1

print(result)