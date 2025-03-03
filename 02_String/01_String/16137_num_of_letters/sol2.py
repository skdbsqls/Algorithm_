import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    my_dict = {}
    for char in str1:
        my_dict[char] = 0

    for char in str2:
        if char in my_dict:
            my_dict[char] += 1

    max_v = 0
    for count in my_dict.values():
        if max_v < count:
            max_v = count

    print(f'#{tc} {max_v}')