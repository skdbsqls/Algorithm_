import sys

sys.stdin = open('sample_input.txt')

# 풀이 1
T = int(input())
for tc in range(1, T + 1):
    arr = list(input())

    stack = []
    result = 0
    for i in range(len(arr)):
        if arr[i] == '(' and arr[i + 1] == ')':
            result += len(stack)
        if arr[i] == '(' and arr[i + 1] != ')':
            stack.append(arr[i])
        if arr[i] == ')' and arr[i - 1] != '(':
            result += 1
            if len(stack):
                stack.pop()

    print(f'#{tc} {result}')

# 풀이2
T = int(input())
for tc in range(1, T + 1):
    iron = list(input())
    total = 0
    stack = []

    for i in range(len(iron)):
        tip = iron[i]

        # 여는 괄호라면
        if tip == '(':
            stack.append(tip)

        # 닫는 괄호인데 이전도 닫는 괄호라면
        elif iron[i - 1] == ')':
            stack.pop()  # 쇠파이프 하나가 끝남
            total += 1  # 쇠파이프가 끝났으므로, total + 1
        # 닫는 괄호인데 이전은 여는 괄호라면(레이저라면)

        else:
            stack.pop()  # 쇠파이브가 아니었으니 뽑아줌
            total += len(stack)  # 남은 쇠파이프 개수만큼 더해줌

    print(f'#{tc} {total}')