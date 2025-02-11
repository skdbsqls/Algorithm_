import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    string = input()

    dict = {
        'b': 'd',
        'd': 'b',
        'p': 'q',
        'q': 'p',
    }
    result = ''

    # 단어 순서대로 거울로 보면 보이는 알파벳으로 바꾸기
    for char in string:
        result += dict[char]

    # 문자열 거꾸로 뒤집기
    result = result[::-1]

    print(f'#{tc} {result}')