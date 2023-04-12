# 전체 경우의 수가 24 * 60 * 60 이므로 86,400개이므로 이는 파이썬에서 시간 제한이 오버되지 않는 경우라고 판단.
# 따라서 삼중 for문 사용해도 크게 지장없으므로 그렇게 풀도록 함.

n = int(input())
count = 0

# 시각 카운트

for hr in range(n+1):
    for min in range(60):
        for sec in range(60):
            if sec % 10 == 3 or sec // 10 == 3:
                count += 1
            elif min % 10 == 3 or min // 10 == 3:
                count += 1
            elif hr % 10 == 3 or hr // 10 == 3:
                count += 1

print(count)
