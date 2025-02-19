import sys

sys.stdin = open('s_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    routes = [list(map(int, input().split())) for _ in range(N)]

    bus_stops = [0] * 5000  # 5000개의 버스 정류장
    # 모든 버스 정류장마다 지나는 버스 노선의 수 구하기
    for route in routes:
        A, B = route

        # A 이상 B 이하인 버스 정류장에 + 1
        for i in range(A - 1, B):
            bus_stops[i] += 1

    P = int(input())
    result = [0] * P  # P개의 버스 정류장
    for i in range(P):
        # C번 버스 정류장을 지나는 버스 노선의 개수 담아주기
        C = int(input())
        result[i] = bus_stops[C - 1]

    print(f'#{tc} {" ".join(map(str, result))}')