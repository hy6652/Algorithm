# 문제: 중복된 문자를 제외하고 사전식 순서로 나열
# 주의: 만약 입력값이 ebcabc이면 결과는 eabc가 된다. 
    # 그 이유는 e 자체는 사전적 순서로 가장 마지막에 위치하지만 입력값에서 딱 한 번만 등장하고 a,b,c는 뒤이어 등장하기 때문에 e의 위치를 변경할 수 없다.
    # 만약 입력값이 ebcabce라면 첫 번째 e는 중복으로 제거하고 마지막 e를 남겨서 결과는 abce가 될 수 있다.

import collections


# 1. 재귀를 이용한 분리
def removeDuplicateLetters(s: str) -> str:
    # 집합으로 정렬
    print(set(s))
    for char in sorted(set(s)):
        suffix = s[s.index(char):]

        # 전체 집합과 접미사 집합이 일치할 때 분리 진행
        if set(s) == set(suffix):
            return char + removeDuplicateLetters(suffix.replace(char, ''))
    return ''


# 2. 스택 이용
def removeDuplicateLetters(s: str) -> str:
    counter, seen, stack = collections.Counter(s), set(), []

    for char in s:
        counter[char] -= 1
        if char in seen:
            continue

        # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
        ## char가 stack에 쌓여 있던 문자보다 앞선 문자이고, stack에 쌓여 있는 문자가 뒤에 남아 있다면(counter[stack[-1]] > 0), 쌓아둔 문자를 제거
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)
        
    return ''.join(stack)


# 2-1 print가 있는 버전
# def removeDuplicateLetters(s: str) -> str:
#     counter, seen, stack = collections.Counter(s), set(), []
#     for char in s:
#         counter[char] -= 1
#         print(counter)
#         print({"char": char})
#         if char in seen:
#             print({"seen": seen})
#             print("============ PASS ============")
#             continue

#         while stack and char < stack[-1] and counter[stack[-1]] > 0:
#             seen.remove(stack.pop())
#         stack.append(char)
#         seen.add(char)

#         print({"stack": stack})
#         print({"seen": seen})
#         print("==============================")
        
#     return ''.join(stack)
