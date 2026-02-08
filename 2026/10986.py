"10986 나머지의 합"

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

# 누적합 배열 만들기
prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + A[i - 1]

# 각 누적합의 나머지 개수 세기
remain_cnt = [0] * M
for i in range(N + 1):
    r = prefix[i] % M
    remain_cnt[r] += 1

# 나머지가 같은 것들끼리 2개씩 뽑는 조합의 수
ans = 0
for cnt in remain_cnt:
    if cnt >= 2:
        ans += cnt * (cnt - 1) // 2

print(ans)