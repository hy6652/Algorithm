# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

from itertools import permutations

# 1 -> 시간초과
def solution(numbers):
    num_list = []
    for item in permutations(numbers, len(numbers)):
        a = ''.join(map(str, list(item)))
        num_list.append(a)
    
    max_num = max(num_list)
    return max_num


# 2
def solution(numbers):
    answer = ''

    nums = list(map(str, numbers))
    # 아스키 코드 기준으로 정렬하기 위해서 자릿수를 세자리 이상으로 통일해주어야 한다.
    # 따라서 x*3을 기준으로 하면, 문자열 3을 세번 곱한 333과 문자열 30을 세번 곱한 303030은 세번째 자리에서 끊어서 비교하게 된다.
    # 그러면 333 > 303이기 때문에 3이 30보다 앞에 위치하게 된다.
    # 네 번째 자릿수부터의 수로 인한 정렬은 큰 의미가 없는데, 이는 세 번째 자릿수까지 서로 같다는 것을 의미한다. 이때는 실제로 같은 수 취급이기 때문에 어떻게 정렬되도 상관없다.
    nums.sort(key = lambda x: x*3, reverse=True)
    answer = int(''.join(nums))

    return str(answer)
    

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))