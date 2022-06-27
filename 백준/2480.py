# 에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다. 

# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다. 
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다. 

a, b, c = map(int, input().split())

if a == b == c:
    prize = 10000 + a * 1000
    print(prize)
elif a == b:
    prize = 1000 + a * 100
    print(prize)
elif a == c:
    prize = 1000 + a * 100
    print(prize)
elif b == c:
    prize = 1000 + b * 100
    print(prize)
else:
    prize = max(a, b, c) * 100
    print(prize)