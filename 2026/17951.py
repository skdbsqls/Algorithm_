"17951 흩날리는 시험지 속에서 내 평점이 느껴진거야"

import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # N: 시험지 개수, K: 나눌 그룹 수
scores = list(map(int, input().split())) # 맞은 문제 개수 리스트

# 이분 탐색 준비
left, right = 0, sum(scores)
ans = 0

# 이분 탐색
while left <= right:
    mid = (left + right) // 2 # 현재 시도하는 평점

    # mid 이상의 평점을 만들 수 있는 그룹 수 계산
    group_cnt = 0 # 만든 그룹 수
    cur_sum = 0 # 현재 그룹의 점수 합

    for score in scores:
        cur_sum += score

        # 현재 그룹의 점수 합이 mid 이상이면 그룹 생성
        if cur_sum >= mid:
            group_cnt += 1
            cur_sum = 0 # 그룹 초기화

    # 그룹 수가 K 이상이면 mid를 정답 후보로 하고 더 큰 값 탐색
    if group_cnt >= K:
        ans = mid
        left = mid + 1
    # 그룹 수가 K 미만이면 mid를 만들 수 없으므로 더 작은 값 탐색
    else:
        right = mid - 1

print(ans)
    