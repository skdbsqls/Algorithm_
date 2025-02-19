import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    [K, N, M] = list(map(int, input().split()))
    charging_stations = list(map(int, input().split()))

    count = 0  # 충전 횟수
    current = 0  # 버스의 현재 위치

    # 도착할 때까지 반복
    while current + K < N:  # N번 정류장까지 이동
        for location in range(current + K, current, -1):  # 현재 위치에서 가장 멀리 갈 수 있는 충전소 찾기
            if location in charging_stations:
                current = location  # 현재 위치 수정
                count += 1  # 충전 횟수 + 1
                break
        # 충전소가 없어서 도착하지 못 하는 경우
        else:
            count = 0
            break

    print(f'#{test_case} {count}')