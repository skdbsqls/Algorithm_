import sys
sys.stdin = open('sample_input (2).txt')

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split()) # 노드의 개수, 리프 노드의 개수, 값을 출력할 노드 번호
    arr = [list(map(int, input().split())) for _ in range(M)]
    tree = [0] * (N + 1)  # 트리

    for node, num in arr:
        tree[node] = num  # 리프 노드의 값 넣어주기

    # 부모 노드 인덱스 =  자식 노드 인덱스 // 2
    for i in range(N, -1, -1):
        tree[i // 2] += tree[i]

    # L번째 노드 번호 출력
    print(f'#{tc} {tree[L]}')