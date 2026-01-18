"2343 기타 레슨"

import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # N개의 강의, M개의 블루레이
lectures = list(map(int, input().split()))  # 강의 리스트(길이)

# 이분 탐색 준비
start = max(lectures)
end = sum(lectures)
ans = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 1  # 블루레이 개수
    total = 0  # 현재 블루레이에 담긴 강의 길이의 총합

    for lecture in lectures:
        # 현재 블루레이에 더 담을 수 있으면 담기
        if total + lecture <= mid:
            total += lecture
        # 현재 블루레이에 더 담을 수 없으면 다음 블루레이에 담기
        else:
            cnt += 1
            total = lecture

    # 블루레이의 개수가 M보다 작으면 블루레이가 더 필요함
    if cnt > M:
        start = mid + 1
    # 블루레이의 크기가 M보다 작으면 블루레이 크기를 저장하고 크기를 줄여봄
    else:
        ans = mid
        end = mid - 1

print(ans)