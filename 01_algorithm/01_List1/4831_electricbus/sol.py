import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1):
    [K, N, M] = list(map(int, input().split()))
    charging_stations = list(map(int, input().split()))

    count = 0  # 충전 횟수
    current = 0  # 버스의 현재 위치

    # 도착할 때까지 반복

    for i in range(current + K, current, -1):
        if i in charging_stations:
            current = i
            count += 1
            break
        else:
            count = 0
            break

        # if count == 0:
        #     break

    print(f'#{test_case} {count}')