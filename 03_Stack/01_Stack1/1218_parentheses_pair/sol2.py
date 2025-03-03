import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    string = input()

    opens = ['(', '[', '{', '<']
    closes = [')', ']', '}', '>']
    stack = []
    result = 1

    for item in string:
        if item in opens:
            stack.append(item)
        elif item in closes:
            if stack:
                open_idx = opens.index(stack[-1])
                close_idx = closes.index(item)

                if open_idx == close_idx:
                    stack.pop()
                else:
                    result = 0
                    break

    if stack:
        result = 0

    print(f'#{tc} {result}')
