# python3

n, m = map(int, input().split())

temp = 0

for i in range(n):
    array = list(map(int, input().split()))
    array.sort()
    temp = max(temp, array[0])

result = temp

print(result)

    