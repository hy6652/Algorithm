# 문제: n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력
## 이 문제에서 배열의 입력값은 항상 2n개, 배열을 오름차순으로 정렬한 후 min에 앞에서 두 개씩 집어넣으면 됨.
## 반대로 정렬 후 뒤에서 두 개씩 집어넣어도 됨.
from typing import List


# 1. 오름차순 풀이
def arrayPariSum(nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
    return sum


# 2. 짝수 번째 값 계산
def arrayPariSum(nums: List[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n
    
    return sum


# 3. 슬라이싱 이용
def arrayPariSum(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])

print(arrayPariSum([1, 4, 3, 2]))