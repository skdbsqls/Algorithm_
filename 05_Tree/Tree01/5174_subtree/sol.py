import sys
sys.stdin = open('sample_input.txt')

def in_order(n, count):
    if n:
        count = in_order(left[n], count)  # 왼쪽 자식으로 이동
        count += 1
        count = in_order(right[n], count)  # 오른쪽 자식으로 이동
    return count

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, (input().split()))  # 간선의 개수, 루트 노드
    arr = list(map(int, input().split()))

    left = [0] * (E + 2)  # 왼쪽 자식
    right = [0] * (E + 2)  # 오른쪽 자식

    # 부모를 인덱스로 자식 저장
    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]

        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    # N을 루트 노드로 하는 서브 트리에 속한 노드의 개수 알아내기
    result = in_order(N, 0)

    print(f'#{tc} {result}')

