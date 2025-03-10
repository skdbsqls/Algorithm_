import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    A, B, C = map(int, input().split())
    ans = -1  # 결과
    cnt = 0  # 사탕의 개수

    # B의 사탕의 개수가 C보다 크거나 같으면 먹어줘야만.
    if B >= C:
        cnt += B - (C - 1)  # 먹어야 하는 사탕의 개수
        B = C - 1  # 최소로 먹어야 하니까 C보다 1만큼만 작으면 됨.

    if A >= B:
        cnt += A - (B - 1)
        A = B - 1

    # 올바른 수열이면서, 빈 상자가 없으면 ans = cnt, 그렇지 않으면 ans =  -1
    if 0 < A < B < C:
        ans = cnt

    print(f'#{tc} {ans}')
