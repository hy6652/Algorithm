# 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 
# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.


# 1 -> 통과하지 못하는 테스트가 있음
# def solution(n, lost, reserve):
#     answer = 0 

#     # 체육복을 가지고 있는 학생 수
#     students = n - len(lost)
#     for i in reserve: # 여분이 있는 학생
#         for j in lost: # 체육복이 없는 학생
#             if (i - 1 == j) or (i + 1 == j):
#                 answer += 1
#                 lost.remove(j)
#     students = students + answer

#     return students


# 2 -> 테스트 두 개 통과 못 함
# def solution(n, lost, reserve):
#     answer = 0

#     for i in range(1, n+1):
#         if i not in lost: # 체육복을 잃어버리지 않은 학생
#             answer += 1
#         else:
#             if i in reserve: # 잃어버렸지만 여분이 있는 학생
#                 answer += 1
#                 reserve.remove(i)
#                 lost.remove(i)

#     for i in lost:
#         if i-1 in reserve:
#             answer += 1
#             reserve.remove(i-1)
#         elif i+1 in reserve:
#             answer += 1
#             reserve.remove(i+1)

#     return answer


# 3
def solution(n, lost, reserve):
    answer = 0
    reserves = set(reserve) - set(lost)
    losts    = set(lost) - set(reserve)

    for i in reserves:
        if i-1 in losts:
            losts.remove(i-1)
        elif i+1 in losts:
            losts.remove(i+1)

    answer = n - len(losts)
    return answer


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))