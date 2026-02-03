"11722 가장 긴 감소하는 부분 수열"

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N # 하나만 있어도 길이가 1

# 각 인덱스를 끝으로 하는 가장 긴 감소하는 부분 수열의 길이 저장
for i in range(N):
    for j in range(i):
        if A[j] > A[i]: # 감소하는
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))