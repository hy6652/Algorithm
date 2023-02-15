# 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.


# 1
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        # 두 번째 케이스의 경우 sort를 하면 3번째에서 if문에 걸려 정답 도출 가능
        if participant[i] != completion[i]:
            return participant[i]
    # 첫 번째 케이스는 sort를 하면 두 리스트의 순서가 같아지고 participant가 원소를 하나 더 가지고 있게 됨. 그걸 return하면 정답 도출 가능.
    return participant[-1]


# 2
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for part, comp in zip(participant, completion):
        if part != comp:
            return part
    return participant[-1]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))