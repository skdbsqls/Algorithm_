import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    string = input()
    stack = []

    for char in string:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    print(f'#{tc} {len(stack)}')