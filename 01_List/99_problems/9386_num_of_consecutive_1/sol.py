import sys

sys.stdin = open('input1.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input()))

    counts = []  # 연속된 1의 개수들을 담은 list
    count = 0  # 연속된 1의 개수

    for i in range(len(nums)):
        # 1이면 count + 1 해주고 counts에 삽입
        if nums[i] == 1:
            count += 1
            counts.append(count)
        # 0이면 count = 0 해주고 counts에 삽입
        else:
            count = 0
            counts.append(count)

    # 연속한 1의 개수 중 최대값 구하기
    result = max(counts)

    print(f'#{tc} {result}')

    # print(nums)
    # print(counts)
    '''
    [0, 0, 1, 1, 0, 0, 1, 1, 1, 0]
    [0, 0, 1, 2, 0, 0, 1, 2, 3, 0]
    '''