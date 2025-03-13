import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 컨테이너 수, 트럭 수
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    # 컨테이너, 트럭 arr 내림차순 정렬
    container.sort(reverse=True)
    truck.sort(reverse=True)

    total = 0  # 최대 화물의 무게
    i = 0  # 컨테이너
    j = 0  # 트럭

    while True:
        # 컨테이너 혹은 트럭을 다 비교할 때까지 반복
        if i == N or j == M:
            break

        # 만약, 컨테이너 > 트럭이면, 옮길 수 없다는 뜻
        if container[i] > truck[j]:
            i += 1   # 다음 컨테이너 확인

        # 만약, 컨테이너 <= 트럭이면, 옮길 수 있다는 뜻
        else:
            total += container[i]  # 무게 추가
            i += 1  # 다음 컨테이너, 트럭 비교
            j += 1

    print(f'#{tc} {total}')