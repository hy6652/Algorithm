# 훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때, 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.
# 첫째 줄에는 현재 시각이 나온다. 두 번째 줄에는 요리하는 데 필요한 시간이 분 단위로 주어진다. 

h, m = map(int, input().split())
time = int(input())

m = m + time

h = h + (m//60)
h = h % 24
m = m % 60


print(h, m)