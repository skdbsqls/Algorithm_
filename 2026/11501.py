"11501 주식"

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input()) # 날의 수
    prices = list(map(int, input().split())) # 날 별 주가

    max_price = 0
    profit = 0

    # 뒤에서부터 탐색
    for i in range(N - 1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        else:
            profit += max_price - prices[i] # 미래의 최댓값 - 오늘 가격 만큼 이익이 생김
        
    print(profit)