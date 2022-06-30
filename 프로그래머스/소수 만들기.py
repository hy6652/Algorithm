# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

from itertools import combinations, count

# 1
def solution(nums):
    sum = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                a = nums[i] + nums[j] + nums[k]
                sum.append(a)
    
    count = 0
    for i in sum:
        total = 0
        for j in range(1, i+1):
            if i % j == 0:
                total += 1
        
        if total == 2:
            count += 1

    return count

# 2
def solution(nums):
    count = 0
    for item in combinations(nums, 3):
        total = sum(item)
        for i in range(2, total):
            if total % i == 0:
                break
        else:
            count+=1
    return count


print(solution([1, 2, 3, 4]))