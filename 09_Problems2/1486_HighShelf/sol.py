import sys
sys.stdin = open('input.txt')


# level: N(직원 수)
# branch: 2 (포함한다, 안 한다)
def recur(cnt, height):
    global min_height

    if height >= B:
        min_height = min(min_height, height)
        return

    if cnt == N:
        return

    recur(cnt + 1, height + heights[cnt])  # 포함한다
    recur(cnt + 1, height)  # 안 한다


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())  # 직원 수, 선반 높이
    heights = list(map(int, input().split()))  # 직원들이 키

    min_height = 1e9
    recur(0, 0)

    print(f'#{tc} {min_height - B}')