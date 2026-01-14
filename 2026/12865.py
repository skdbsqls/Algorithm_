import sys
input = sys.stdin.readline

# 물건 개수 N, 배낭 최대 무게 K
N, K = map(int, input().split())

# 물건 정보 (무게, 가치)
items = [(0, 0)]
for _ in range(N):
    w, v = map(int, input().split())
    items.append((w, v))

# dp[i][w]
# i번째 물건까지 고려했을 때
# 배낭 용량이 w일 때 얻을 수 있는 최대 가치
dp = [[0] * (K + 1) for _ in range(N + 1)]

# DP 채우기
for i in range(1, N + 1):
    wi, vi = items[i] # i번째 물건의 무게, 가치

    for w in range(K + 1):
        # ① i번째 물건을 안 넣는 경우
        dp[i][w] = dp[i - 1][w]

        # ② i번째 물건을 넣을 수 있는 경우
        if w >= wi:
            dp[i][w] = max(
                dp[i][w],
                dp[i - 1][w - wi] + vi
            )

print(dp[N][K])
