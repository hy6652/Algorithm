# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.


# 1 -> 런타임 에러
# def solution(answers):
#     # answers의 길이에 맞춰 first의 정답 길이 조절
#     length = len(answers)
#     first = [1, 2, 3, 4, 5]
#     i = int(length / len(first))

#     if i < 1:
#         first = first[:length]
#     else:
#         first = first * i
    
#     # answers와 first의 답 비교
#     first_correct = []
#     for ind in range(length):
#         if first[ind] == answers[ind]:
#             first_correct.append(first[ind])

#     # 위의 과정 반복
#     second = [2, 1, 2, 3, 2, 4, 2, 5] 
#     j = int(length / len(second))

#     if j < 1:
#         second = second[:length]
#     else:
#         second = second * j
    
#     second_correct = []
#     for ind in range(length):
#         if second[ind] == answers[ind]:
#             second_correct.append(second[ind])

#     third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
#     k = int(length / len(third))

#     if k < 1:
#         third = third[:length]
#     else:
#         third = third * k

#     third_correct = []
#     for ind in range(length):
#         if third[ind] == answers[ind]:
#             third_correct.append(third[ind])

#     # 맞은 개수 비교하여 제일 많이 맞은 사람 return
#     who_answer = [1, 2, 3]
#     corrects = [len(first_correct),  len(second_correct), len(third_correct)]
#     max_correct = max(corrects)
#     answer_zip = zip(who_answer, corrects)

#     answer = []
#     for key, value in answer_zip:
#         if value == max_correct:
#             answer.append(key)

#     return answer


# 2
def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5] 
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    solver = [0, 0, 0]
    for i in range(len(answers)):
        # first, second, third의 값이 결국 반복되는 때문에 index를 i % len()으로 잡는다.
        if answers[i] == first[i % len(first)]:
            solver[0] += 1
        if answers[i] == second[i % len(second)]:
            solver[1] += 1
        if answers[i] == third[i % len(third)]:
            solver[2] += 1
    
    answer = []
    for i in range(len(solver)):
        if solver[i] == max(solver):
            answer.append(i+1)
    return answer

print(solution([1, 2, 3, 4, 5]))