import sys
import operator

sys.stdin = open('input.txt')

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}


# 연산하기
def in_order(n):
    if n:
        left_c = elements[int(left[n])]  # 왼쪽 자식(피연산자)
        operator = elements[n]  # 연산자
        right_c = elements[int(right[n])]  # 오른쪽 자식(피연산자)
        # result = eval(f'{left_c}{operator}{right_c}')
        result = ops[operator](int(left_c), int(right_c))  # 연산하기
        return result


for tc in range(1, 11):
    N = int(input())  # 정점의 개수
    elements = [''] * (N + 1)  # 연산자 혹은 정수(정점의 요소) 저장
    left = [0] * (N + 1)  # 왼쪽 자식 저장
    right = [0] * (N + 1)  # 오른쪽 자식 저장

    for _ in range(N):
        arr = input().split()
        p = int(arr[0])  # 정점 번호

        # 정점의 요소 저장
        elements[p] = arr[1]
        # 왼쪽 자식 저장
        if len(arr) > 2:
            left[p] = arr[2]
        # 오른쪽 자식 저장
        if len(arr) > 3:
            right[p] = arr[3]

    # 마지막 연산자 찾기
    operators = ['+', '-', '*', '/']
    # 뒤에서부터 계산
    for i in range(len(elements) - 1, 0, -1):
        if elements[i] in operators:  # 연산자라면
            # 중위순회? (연산하기)
            elements[i] = in_order(i)

    print(f'#{tc} {int(elements[1])}')