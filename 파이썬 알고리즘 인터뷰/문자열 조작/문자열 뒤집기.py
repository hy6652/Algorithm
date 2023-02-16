# 문제: 문자열을 뒤집는 함수를 작성. 입력값은 문자 배열, 리턴 없이 리스트 내부를 직접 조작
from typing import List

## 1. 투 포인터 사용
def reverseString(s: List[str]) -> None:
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


# 2. 파이썬 함수
def reverseSting(s: List[str]) -> None:
    s.reverse()
