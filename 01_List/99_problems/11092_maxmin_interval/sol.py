import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    # 최소값의 위치 구하기 (뒤에서부터)
    min_v = nums[-1]  # 최소값
    min_idx = 0  # 최소값의 인덱스
    for i in range(N - 1, -1, -1):
        if min_v >= nums[i]:
            min_v = nums[i]
            min_idx = i + 1

    # 최대값의 위치 구하기 (앞에서부터)
    max_v = nums[0]  # 최대
    max_idx = 0  # 최대값의 인덱스
    for i in range(0, N):
        if max_v <= nums[i]:
            max_v = nums[i]
            max_idx = i + 1

    # 간격 구하기
    result = abs(min_idx - max_idx)

    print(f'#{tc} {result}')