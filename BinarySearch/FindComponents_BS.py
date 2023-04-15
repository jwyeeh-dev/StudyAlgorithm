n = int(input())
stocks = list(map(int, input().split()))

m = int(input())
needs = list(map(int, input().split()))

results = []

def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2

    if array[mid] == target:
        return 'yes'
    
    elif array[mid] > target:
        binary_search(array, target, start, mid - 1)
    
    else:
        binary_search(array, target, mid + 1, end)

        


for need in needs:
        results.append(binary_search(stocks, need, 0, len(stocks) - 1))


for result in results:
    if result is None:
        print('no', end = " ")
    else:
        print(result, end = " ")