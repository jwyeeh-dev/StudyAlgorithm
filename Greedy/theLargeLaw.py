n, m, k = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

lar1 = array[n-1]
lar2 = array[n-2]


result = 0

while m > 0:
  if m <= k:
    for i in range(m):
      result = result + lar1
      m = m - 1

  if m > k:
    for i in range(k):
      result = result + lar1
      m = m - 1

    result = result + lar2
    m = m - 1

print(result)
