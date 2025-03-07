import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 세로, 가로
    matrix = [input() for _ in range(N)]

    # 숨겨진 암호 코드 모두 찾아내기
    codes = []
    for i in range(N):
        temp = ''
        for j in range(M - 1, -1, -1):  # 뒤에서 부터
            temp += matrix[i][j]  # temp에 담아주기

        # 이미 발견한 암호 코드가 아니라면
        if temp and temp not in codes:
            codes.append(temp)  # codes에 담아주기

    # codes에 있는 암호 코드들 2진수로 바꿔주기
    hex_digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for i in range(len(codes)):
        # 16진수를 10진수로 바꾸기
        dec_num = []
        for digit in codes[i]:
            dec_num.append(hex_digit.index(digit))  # 해당 16진수의 인덱스 값 = 10진수

        # 10진수를 2진수로 바꾸기
        bin_nums = ''
        for num in dec_num:
            bin_num = ''
            while num > 0:  # 2진수로 바꾸기
                remain = num % 2
                bin_num = str(remain) + bin_num
                num //= 2
            if len(bin_num) < 4:  # 2진수의 앞자리 0 만들기
                while len(bin_num) < 4:
                    bin_num = '0' + bin_num
            bin_nums += bin_num
        codes[i] = bin_nums

    # code 정비... 앞에 있는 0 빼기.. 그니까 맨 뒤에 있는 0 빼기..
    real_codes = []
    for code in codes:
        for i in range(len(code)):
            if code[i] != '0':
                real_codes.append(code[i:])
                break

    for code in real_codes:
        if len(code) // 56 == 0:
            temp = 1
        else:
            temp = len(code) // 56

        for i in range(1, temp + 1):
            for j in range(len(code), -1, -(7 * i)):
                num = code[j:j + 7]