# 재귀함수는 수학의 점화식(재귀식)을 그대로 소스코드로 옮겼기 때문에 코드의 길이가 더 간결해지는 이점이 있음.
# 하지만 재귀함수는 무한 루프 동작을 방지하기 위하여 if문을 통한 종료 조건을 반드시 구현해줄 필요가 있음.

def recursive_function(i):
    if i == 100:
        return
    print(i, '번쨰 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀 함수를 종료합니다.')


def factorial_iterative(n):
    result = 1

    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

print('반복적으로 구현 : ', factorial_iterative(5))
print('재귀적으로 구현 : ', factorial_recursive(5))

