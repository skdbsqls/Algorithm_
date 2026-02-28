"2133 타일 채우기"

import sys
input = sys.stdin.readline

N = int(input())

# N이 홀수면 채울 수가 없음
if N % 2 == 1:
    print(0)
    sys.exit(0)

dp = [0] * (N + 1)
dp[0] = 1
dp[2] = 3

# 점화식: dp[n] = 3⋅dp[n−2] + 2⋅(dp[n−4] + dp[n−6] + ⋯ + dp[0])
for i in range(4, N + 1, 2): # 짝수만 채우면 됨
    dp[i] = 3 * dp[i - 2]
    for j in range(i - 4, -1, -2):
        dp[i] += 2 * dp[j]

print(dp[N])