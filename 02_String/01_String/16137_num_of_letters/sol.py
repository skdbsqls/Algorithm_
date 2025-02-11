import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    # str1의 글자들 딕셔너리로 만들기
    dict = {}
    for char in str1:
        dict[char] = 0

    # str1에 포함된 글자들이 str2 몇 개 있는지 확인
    for char in str2:
        if char in dict:
            dict[char] += 1

    # 가장 많은 글자의 개수 구하기
    result = 0
    for count in dict.values():
        if result < count:
            result = count

    print(f'#{tc} {result}')