# 문제: 가장 긴 팰린드롬 부분 문자열 출력

def longestPalindrome(s: str) -> str:
    # 첫 팰린드롬을 발견한 후에는 양 옆으로 포인터를 확장
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # 한 칸씩 확장
            left -= 1
            right += 1
        return s[left+1 : right]
    
    if len(s) < 2 or s == s[::-1]:
        return s
    
    result = ''
    # 슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        result = max(
                    result,
                    expand(i, i+1),
                    expand(i, i+2),
                    key=len
                )
    return result
