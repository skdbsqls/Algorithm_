"15486 퇴사 2"

import sys
input = sys.stdin.readline

N = int(input())
T = [0] * (N + 2)
P = [0] * (N + 2)

for i in range(1, N + 1):
    t, p = map(int, input().split())
    T[i] = t
    P[i] = p

# dp[i]: i번재 날까지 봤을 때, 얻을 수 있는 최대 수익
dp = [0] * (N + 2)

for i in range(1, N + 2):
    # i일에 상담을 안 해도 어제까지 벌어놓은 돈은 유지
    dp[i] = max(dp[i], dp[i - 1])

    # i일에 시작하는 상담이 퇴사 전에 끝나면(가능)
    end = i + T[i]
    if end <= N + 1:
        dp[end] = max(dp[end], dp[i] + P[i])

print(dp[N + 1])
