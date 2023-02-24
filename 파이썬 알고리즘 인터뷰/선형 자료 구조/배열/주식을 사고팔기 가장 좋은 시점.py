# 문제: 한 번의 거래로 낼 수 있는 최대 이익 산출
import sys
from typing import List

# 1. 저점과 현재 값과의 차이 계산
def maxProfit(prices: List[int]) -> int:
    # 최댓값의 변수인 profit과 최솟값의 변수인 min_price과 다른 값과 비교된 후 바로 교체될 수 있도록 각각 최솟값, 최댓값으로 설정
    profit = 0
    min_price = sys.maxsize
    
    for price in prices:
        min_price = min(min_price, price)
        # profit은 price-min_price의 격차가 가장 큰 것을 고른다
        profit = max(profit, price - min_price)
    
    return profit

maxProfit([7, 1, 5, 3, 6, 4])