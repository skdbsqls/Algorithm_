"15686 치킨 배달"

import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses = [] # 집 좌표
chickens = [] # 치킨집 좌표

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

ans = float('inf')

# 치킨집 중에서 M개를 고르는 모든 조합
for selected in combinations(chickens, M):
    chicken_dist = 0 # 도시 치킨 거리

    # 모든 집에 대해
    for hx, hy in houses:
        min_dist = float('inf') # 가장 가까운 치킨집 거리

        # 선택된 치킨집들 중에서 가장 가까운 치킨 거리 구하기
        for cx, cy in selected:
            dist = abs(hx - cx) + abs(hy - cy)
            min_dist = min(min_dist, dist)
        
        chicken_dist += min_dist

    ans = min(ans, chicken_dist)

print(ans)