"2512 예산"

import sys
input = sys.stdin.readline

N = int(input())
requests = list(map(int, input().split()))
M = int(input())

# 요청 예산의 합이 예산 총액보다 큰 경우 총합 구하는 함수
def sum_total(m_value, requests):
    total = 0
    for request in requests:
        if request > m_value:
            total += m_value
        else:
            total += request
    return total


# 요청 예산 총합이 예산 총액보다 같거나 작은 경우
if sum(requests) <= M:
    print(max(requests))
# 그렇지 않은 경우
else:
    # 이분 탐색으로 상한액 구하기
    start, end = 0, max(requests)
    ans = 0

    while start <= end:
        mid = (start + end) // 2
        total = sum_total(mid, requests)

        if total <= M:
            ans = mid         
            start = mid + 1
        else:
            end = mid - 1

    print(ans)