import sys

sys.stdin = open('sample_input.txt')

for test_case in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    result = 0  # 조망권이 확보된 칸의 수
    for j in range(N):
        # 만약 건물의 높이가 0이면 볼 필요 없음
        if arr[j] == 0:
            continue

        # arr[j]를 기준으로 좌우 2칸
        buildings = [arr[j-2], arr[j-1], arr[j+1], arr[j+2]]

        # 좌우 2칸 중 가장 높은 건물 찾기
        highest = buildings[0]
        for building in buildings:
            if highest < building:
                highest = building

        # arr[j](= 기준 건물)가 좌우 2칸 내에서 가장 높은 건물이면,
        # (기준 건물 - 좌우 2칸 중 가장 높은 건물) 만큼 조망권 확보
        if arr[j] > highest:
            view = arr[j] - highest  # 기준 건물이 확보한 조망권 칸의 수
            result += view

    print(f'#{test_case} {result}')