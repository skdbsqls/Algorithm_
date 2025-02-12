import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    A, B = (input().split())
    A_lst = list(A)

    result = 0
    i = 0
    while i < len(A_lst):
        temp = A_lst[i: i + len(B)]

        if ''.join(temp) == B:
            result += 1
            i += len(B)
        else:
            result += 1
            i += 1

    print(f'#{tc} {result}')