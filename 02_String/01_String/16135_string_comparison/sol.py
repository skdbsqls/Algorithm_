import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    result = 0
    for i in range(len(str2) - len(str1) + 1):
        # i번째부터 존재를 확인할 단어(str1)의 길이 만큼 자르기
        word = str2[i: i + len(str1)]

        # 일치 하는지 비교하기
        if word == str1:
            result = 1
            break

    print(f'#{tc} {result}')