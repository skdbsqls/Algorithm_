"14002 가장 긴 증가하는 부분 수열 4"

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N
prev = [-1] * N

for i in range(N):
    for j in range(i):
        if A[j] < A[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            prev[i] = j

# LIS 최대 길이와 끝나는 위치 찾기
max_len = max(dp)
idx = dp.index(max_len)

# 역추적
result = []
while idx != -1:
    result.append(A[idx])
    idx = prev[idx]

result.reverse()

print(max_len)
print(*result)