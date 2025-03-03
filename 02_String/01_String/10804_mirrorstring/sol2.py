import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    string = input()
    my_dict = {
        'b': 'd',
        'd': 'b',
        'p': 'q',
        'q': 'p',
    }

    result = ''
    for i in range(len(string) - 1, -1, -1):
        result += my_dict[string[i]]

    print(f'#{tc} {result}')