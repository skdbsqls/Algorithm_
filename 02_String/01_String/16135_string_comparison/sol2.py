import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    result = 0

    for i in range(len(str2) - len(str1) + 1):  # 인덱스 잘 확인하기
        temp = str2[i:i + len(str1)]

        if temp == str1:
            result = 1
            break

    print(f'#{tc} {result}')
