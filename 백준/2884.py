# 첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 
# 원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸는 것

h, m = map(int, input().split())

if m >= 45:
    m = m - 45
    print(h, m)
elif m < 45 and h >= 1:
    h = h - 1
    m = m + 15
    print(h, m)
elif m < 45 and h == 0:
    h = 23
    m = m + 15
    print(h, m)