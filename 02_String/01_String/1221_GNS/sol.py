import sys

sys.stdin = open('GNS_test_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    tc, count = input().split()
    count = int(count)
    arr = input().split()
    nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    # 문자를 숫자로 바꾸기
    for i in range(len(arr)):
        arr[i] = nums.index(arr[i])

    arr.sort()  # 정렬

    # 숫자를 문자로 바꾸기
    for i in range(len(arr)):
        arr[i] = nums[arr[i]]

    print(f'{tc}')
    print(f'{" ".join(arr)}')