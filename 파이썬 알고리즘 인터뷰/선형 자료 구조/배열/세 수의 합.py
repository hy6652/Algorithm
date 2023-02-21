# 문제: 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트 리턴
from typing import List

# 1. 투 포인터
def sum(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    for i in range(len(nums)-2):
        # 중복된 값 건너 뛰기
        # nums[i-1]로 한 이유는, 이미 i-1번째를 처리했기 때문에 i와 그 앞 값을 비교한다.
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i+1, len(nums)-1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                results.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1

                left += 1
                right -= 1
    return results

sum([-1, 0, 1, 2, -1, -4])
