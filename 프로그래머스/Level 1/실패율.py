# 실패율은 다음과 같이 정의한다 -> 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

# 1 -> 런타임 에러 발생
def solution(N, stages):
    answer = []
    length = len(stages)

    # 1~N까지 스테이지 살피기
    for i in range(1, N+1): # 2, 1, 2, 6, 2, 4, 3, 3
        if len(stages) != 0:
            # 스테이지를 클리어 하지 못한 플레이어 수 계산
            count = stages.count(i) # 2->3개
            # 실패율
            fail = count / length
        else:
            fail = 0
        # 다음 스테이지에 도달한 플레이어 수
        length -= count
        
        # (스테이지 번호, 실패율)
        answer.append((i, fail))

    # 내림차순으로 정렬
    # key = lambda x: x[1] -> 정렬 기준을 실패율로 한다는 의미. x가 answer, x[1]은 answer의 1번째 값.
    answer = sorted(answer, key=lambda x: x[1], reverse=True)
    # 내림차순으로 정렬한 것에서 스테이지 번호 뽑기
    answer = [i[0] for i in answer]
    return answer


# 2
def solution(N, stages):
    answer = {}
    length = len(stages)
    for i in range(1, N+1):
        if length != 0:
            count = stages.count(i)
            answer[i] = count/length
            length -= count
        else:
            answer[i] = 0

    return sorted(answer, key=lambda x: answer[x], reverse=True)

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))