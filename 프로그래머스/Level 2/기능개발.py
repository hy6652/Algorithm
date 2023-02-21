# 프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
# 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.
# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

# 1. progresses와 speeds를 계속 더해가서 첫 번째 값이 100 이상이 된 순간부터 계산 시작
def solution(progresses, speeds):
    answer = []

    while progresses:
        cnt = 0

        progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]

        while progresses and progresses[0] >= 100:
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)

        if cnt:
            answer.append(cnt)
    return answer


# 2. progresses를 다 처리하기 위해 필요한 일수를 구해, 해당 일수들을 비교
def solution(progresses, speeds):
    import math

    days = []
    for i in range(len(progresses)):
        left = math.ceil((100 - progresses[i]) / speeds[i])
        days.append(left)
    
    current = days[0]
    answer  = []
    cnt     = 0
    for day in days:
        if day <= days[0]:
            cnt += 1
        else:
            answer.append(cnt)
            current = day
            cnt = 1
    answer.append(cnt)
    return answer



solution([93, 30, 55], [1, 30, 5])