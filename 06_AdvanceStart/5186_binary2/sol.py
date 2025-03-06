import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = float(input())

    ans = ''
    while 0 < N < 1:
        if N * 2 >= 1:
            ans += '1'
            N = N * 2 - 1
        else:
            ans += '0'
            N *= 2

    if len(ans) > 12:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {"".join(map(str, ans))}')

# T = int(input())
# for tc in range(1, T + 1):
#     N = float(input())
#
#     ans = []
#     while N != 0.0:
#         result = list(map(int, str(N * 2).split('.')))
#         M = result[0]
#         N = float('0.' + str(result[1]))
#         ans.append(M)
#
#         if len(ans) > 12:
#             break
#
#     if len(ans) == 13:
#         print(f'#{tc} overflow')
#     else:
#         print(f'#{tc} {"".join(map(str, ans))}')
