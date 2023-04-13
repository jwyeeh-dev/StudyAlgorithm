# 정렬 알고리즘

## 선택 정렬 (Selection Sort)

- 선택 정렬의 시간복잡도는 O(N^2)이라고 할 수 있습니다.
- 그렇기에 데이터가 늘어나는 경우 정렬 속도가 급격히 늘어날 수 있습니다.
- 하지만 코딩테스트에서는 **특정한 리스트에서 가장 작은 데이터를 찾는 일**이 매우 자주 등장하므로 아래의 소스코드 형태에 익숙해질 필요가 있습니다.

```python
array = [ 데이터가 들어가 있다고 생각해주세요. ] # 정렬이 되어야 할 배열이라고 가정.

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스

    for j in range(i + 1, len(array)): # 정렬된 것을 제외한 나머지 원소
        if array[min_index] > array[j]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i] # 상호 교환 
    # 상호 교환(Swap)은 파이썬에서는 위와 같이 간단하게 구현할 수 있지만, 대부분 프로그래밍 언어에서는 명시적으로 임시 저장용 변수를 만들어 두 원소의 값을 변경해야 합니다.

print(array)
```

### 삽입 정렬 (Insertion Sort)
