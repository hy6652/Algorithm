# 문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.

def solution(s):
    s = s.split(" ")

    num_list = [int(i) for i in s]

    min_num = min(num_list)
    max_num = max(num_list)

    return f"{min_num} {max_num}"


solution("-1 -2 -3 -4")
solution("1 2 3 4")