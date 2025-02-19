import sys

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_v = arr[0]
    max_v = arr[0]

    for num in arr:
        if min_v > num:
            min_v = num
        if max_v < num:
            max_v = num

    result = max_v - min_v

    print(f'#{test_case} {result}')