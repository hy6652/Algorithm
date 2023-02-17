# 문제: 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력. 대소문자 구분 x, 구두점 무시
from typing import List
import re, collections


def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', '', paragraph).lower().split() if word not in banned]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]