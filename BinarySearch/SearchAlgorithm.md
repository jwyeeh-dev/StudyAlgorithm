# 탐색 알고리즘

## 순차 탐색

```python
def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1
        
print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요 : ")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

print(sequential_search(n, target, array))

```

## 이진 탐색

이진 탐색은 중간점이 탐색을 계속 반복하여 행하는 알고리즘이기 때문에 재귀함수를 사용하거나 for문을 활용하여 반복을 수행하는 것이 정석적입니다.
이러한 이진 탐색 소스 코드가 활용될 문제가 매우 많이 나오게 되므로 해당 코드문은 외워두는 것이 좋습니다.

**재귀함수를 활용한 이진 탐색**
```python
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 목표값을 찾은 경우 중간점의 인덱스를 반환
    if array[mid] == target: 
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```

**for문을 활용한 이진 탐색**
```python
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        
        elif array[mid] > target:
            end = mid + 1

        else:
            start = mid + 1
    return None

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```