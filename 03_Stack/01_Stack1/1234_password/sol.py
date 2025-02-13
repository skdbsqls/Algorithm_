import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    N, nums = input().split()
    N = int(N)
    nums = list(nums)

    password = []
    for num in nums:
        if len(password) and password[-1] == num:
            password.pop()
        else:
            password.append(num)

    print(f'#{tc} {"".join(password)}')