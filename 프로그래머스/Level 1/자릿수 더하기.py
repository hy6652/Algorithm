# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

def solution(n):
    number_list = []
    for i in str(n):
        number_list.append(int(i))
    total = sum(number_list)
    return total


def solution(n):
    number_list = []
    while (n != 0):
        number_list.append(n%10)
        n = n // 10
        
    return sum(number_list)

print(solution(192))