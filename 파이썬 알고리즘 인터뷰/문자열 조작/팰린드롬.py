# 문제: 주어진 문자열이 팬린드롬인지 확인, 대소문자를 구분하지 않으며 영문자와 숫자만을 대상으로 함
## 팬린드롬: 앞뒤가 똑같은 단어나 문장, "소주 만 병만 주소"

import collections
from typing import Deque


## 1. 리스트
def isPalindrome(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    # 리스트 앞 뒤 값을 가져와서 같은지 판별
    while len(str) > 1:
        if strs.pop(0) != strs.pop():
            return False
    
    return True


## 2. 데크 자료형 -> 자세한 설명은 노션에
def isPalindrome(s: str) -> bool:
    
    # 자료형을 데크로 선언
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    
    return True
