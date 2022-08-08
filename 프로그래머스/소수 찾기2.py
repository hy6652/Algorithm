# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.


from itertools import permutations

def check(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0

    num = []
    for i in range(1, len(numbers)+1):
        # permutations는 numbers에서 i만큼의 길이로 순열을 반환한다. [['1', '7'], ['17', '71']]
        # permutations으로 만들어진 순열을 ''.join을 통해 합치고, 그걸 set을 통해 중복을 제거한 다음, list로 묶는다.
        num.append(list(set(map(''.join, permutations(numbers, i)))))

    # sum(num, [])를 하면 num을 더해주는데 그러면 [] + ['1', '7'] + ['17', '71']이 되어 리스트끼리의 덧셈이 되어 [1, 7, 17, 71]이 된다.
    item = list(set(map(int, sum(num, []))))
    
    for element in item:
        if check(element) == True:
            answer += 1

    return answer

print(solution("17"))
print(solution("011"))