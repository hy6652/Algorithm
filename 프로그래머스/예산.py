# 최대한 많은 부서의 물품을 구매해 줄 수 있도록 하려고 합니다.
# 물품을 구매해 줄 때는 각 부서가 신청한 금액만큼을 모두 지원해 줘야 합니다. 예를 들어 1,000원을 신청한 부서에는 정확히 1,000원을 지원해야 하며, 1,000원보다 적은 금액을 지원해 줄 수는 없습니다.
# 부서별로 신청한 금액이 들어있는 배열 d와 예산 budget이 매개변수로 주어질 때, 최대 몇 개의 부서에 물품을 지원할 수 있는지 return 하도록 solution 함수를 완성해주세요.

# 1
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()

    length = len(d)
    return length

print(solution([1, 3, 2, 5, 4], 9))