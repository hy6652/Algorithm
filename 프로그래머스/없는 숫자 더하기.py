# 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다. numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.

# 1
def solution(numbers):
    sum = 0
    for i in range(0, 10):
        if i not in numbers:
            sum += i
    return sum

# 2
def solution(numbers):
    return 45 - sum(numbers)

print(solution([1,2,3,4,6,7,8,0]))
