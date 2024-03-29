# 어떤 정수들이 있습니다.
# 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 
# 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.

# 1
def solution(absolutes, signs):
    signs_dict = zip(absolutes, signs)
    sum = 0
    for i, j in signs_dict:
        if j == True:
            sum += i
        else:
            sum += -i

    return sum


# 2
def solution(absolutes, signs):
    return sum(absolute if sign else -absolute for absolute, sign in zip(absolutes, signs))

print(solution([4, 7, 12], [True, False, True]))