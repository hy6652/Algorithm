# 문제: 문자열 배열을 받아 애너그램 단위로 그룹핑
## 애너그램: 문자를 재배열하여 다른 듯을 가진 단어로 바꾸는것, eat - ate - tea
import collections
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        # sorted() -> 인자를 정렬해서 리스트로 반환
        anagrams[''.join(sorted(word))].append(word)    
    return list(anagrams.values())

groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])