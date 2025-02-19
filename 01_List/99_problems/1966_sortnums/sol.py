import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    counts = [0] * (max(arr) + 1)  # 카운트 배열
    result = [0] * len(arr)  # 정렬된 배열

    for i in range(len(arr)):
        counts[arr[i]] += 1

    for i in range(1, max(arr) + 1):
        counts[i] += counts[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        counts[arr[i]] -= 1
        result[counts[arr[i]]] = arr[i]

    print(f'#{tc} {" ".join(map(str, result))}')