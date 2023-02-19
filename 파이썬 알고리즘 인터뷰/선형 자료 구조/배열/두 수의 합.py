# 문제: 덧셈을 하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스 리턴
from typing import List


# 1. in 을 이용한 탐색
def toSum(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        # 0: 2, 1: 7 ...
        complement = target - n

        # target이 되려면 두 수의 합이어야 하니까, target에서 n만큼 뺀 수가 있는지 확인
        if complement in nums[i+1:]:
            return [nums.index(n), nums[i+1:].index(complement) + (i+1)]


# 2. 첫 번째 수를 뺀 결과 키 조회
def toSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i
    
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


# 3. 조회 구조 개선
## 2에서는 두 개의 for문으로 처리하고 3에서는 한 개로 줄였지만, 두 번째 값을 찾기 위해 매번 비교해야하기 때문에 2의 풀이와 비교해 성능상의 큰 이점은 없음
def toSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target-num], i]
        nums_map[num] = i


# 4. 투 포인터 이용
## 하지만 여기서는 nums가 정렬된 상태가 아니기 때문에 포인터로 풀이를 할 수 없다.
## 정렬을 하면 인덱스가 엉망이 된다.
## 인덱스를 찾는 문제가 아니라 값을 찾아내는 문제라면 사용가능
def toSum(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while not left == right:
        # 합이 타겟보다 작으면 왼쪽 포인터 오른쪽으로 이동
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로 이동
        if nums[left] + nums[right] > target:
            right += 1
        else: return [left, right]


toSum([2, 7, 11, 15], 9)
