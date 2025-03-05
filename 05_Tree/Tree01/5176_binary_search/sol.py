import sys
sys.stdin = open('sample_input.txt')


def in_order(n, k):
    if n:
        k = in_order(left[n], k)  # 왼쪽 자식으로 이동
        tree[n] = k  # 숫자 넣기
        k += 1
        k = in_order(right[n], k)  # 오른쪽 자식으로 이동
    return k


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)  # 이진 탐색 트리
    left = [0] * (N + 1)  # 왼쪽 자식
    right = [0] * (N + 1)  # 오른쪽 자식

    # 완전 이진 트리 만들기
    if N % 2 == 0:
        for i in range(1, N // 2 + 1):
            left[i] = i * 2
        for i in range(1, N // 2):
            right[i] = i * 2 + 1
    else:
        for i in range(1, N // 2 + 1):
            left[i] = i * 2
        for i in range(1, N // 2 + 1):
            right[i] = i * 2 + 1

    # 중위 순회 하면서 이진 탐색 트리 만들기
    in_order(1, 1)

    print(f'#{tc} {tree[1]} {tree[N//2]}')