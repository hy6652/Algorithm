# 로그 재정렬
# 기준: 로그의 가장 앞 부분은 식별자, 문자로 구성된 로그가 숫자 로그보다 앞에 위치,
#       식별자는 순서에 영향을 끼치지 않음, 문자가 동일한 경우 식별자 순으로 한다.
#       숫자 로그는 입력 순서대로 한다.
from typing import List


def reorderLogFiles(logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    
    # lambda x: (기준1, 기준2) -> 기준 1로 정렬을 하고, 문자열이 같으면 기준 2로 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits
