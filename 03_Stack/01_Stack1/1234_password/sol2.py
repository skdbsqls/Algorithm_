import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N, nums = input().split()

    stack = []
    for num in nums:
        if stack and stack[-1] == num:
            stack.pop()
        else:
            stack.append(num)

    print(f'#{tc} {"".join(stack)}')