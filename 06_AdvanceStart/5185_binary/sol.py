import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, hex_num = input().split()
    hex_digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    # 16진수를 10진수로 바꾸기
    dec_num = []
    for num in hex_num:
        dec_num.append(hex_digit.index(num))  # 해당 16진수의 인덱스 값 = 10진수

    # 10진수를 2진수로 바꾸기
    result = ''
    for num in dec_num:
        bin_num = ''

        while num > 0:  # 2진수로 바꾸기
            remain = num % 2
            bin_num = str(remain) + bin_num
            num //= 2

        if len(bin_num) < 4:  # 2진수의 앞자리 0 만들기
            while len(bin_num) < 4:
                bin_num = '0' + bin_num

        result += bin_num

    print(f'#{tc} {result}')