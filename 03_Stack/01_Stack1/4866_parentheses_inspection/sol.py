import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    string = list(input())

    result = 1
    stack = []
    for char in string:
        if char == '(' or char == '{':
            stack.append(char)
        elif char == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                result = 0
                break
        elif char == '}':
            if not stack:
                result = 0
                break
            elif stack[-1] == '{':
                stack.pop()

    if len(stack):
        result = 0

    print(f'#{tc} {result}')