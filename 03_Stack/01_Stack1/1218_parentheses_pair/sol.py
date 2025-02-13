import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    string = list(input())

    result = 1
    stack = []
    opens = ['(', '[', '{', '<']
    close = [')', ']', '}', '>']

    for char in string:
        if char in opens:
            stack.append(char)
        elif char in close:
            # if not stack:
            #     result = 0
            #     break
            # if close.index(char) == opens.index(stack[-1]):
            #     stack.pop()
            if len(stack) > 0 and close.index(char) == opens.index(stack[-1]):
                stack.pop()
            else:
                result = 0
                break

    if len(stack):
        result = 0

    print(f'#{tc} {result}')
