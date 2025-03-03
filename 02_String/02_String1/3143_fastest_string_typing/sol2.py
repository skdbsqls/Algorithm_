import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    A, B = input().split()

    A_len = len(A)
    B_len = len(B)
    i = 0
    count = 0
    while i < A_len:
        if A[i:i + B_len] == B:
            i = i + B_len
        else:
            i += 1

        count += 1

    print(f'#{tc} {count}')