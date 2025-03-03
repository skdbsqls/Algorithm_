import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    sentence = input()

    stack = []
    result = 1
    for char in sentence:
        if char == '(' or char == '{':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result = 0
                break
        elif char == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                result = 0
                break

    if stack:
        result = 0

    print(f'#{tc} {result}')
