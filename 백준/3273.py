# 두 수의 합
# n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다. 자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.
import sys

n        = int(input())  # 수열의 크기
num_list = list(map(int, sys.stdin.readline().split()))  # 수열의 수들
target   = int(input())  # 두 수의 합

num_list.sort()
left, right = 0, len(num_list) - 1

count = 0
while not left == right:
    if num_list[left] + num_list[right] > target:
        right -= 1
    elif num_list[left] + num_list[right] < target:
        left += 1
    else:
        # 처음에는 이 경우에 rigth -= 1도 있었는데, 두 수의 합이 타겟과 같아지더라도 다음 수와의 합도 봐야 하기 때문에 left만 이동
        left += 1
        count += 1
        
print(count)