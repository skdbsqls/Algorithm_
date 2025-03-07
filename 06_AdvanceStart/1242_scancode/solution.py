import sys
sys.stdin = open('sample_input.txt')

# 16진수를 2진수로 변환하는 dictionary
hex_to_bin = {
    '0': [0, 0, 0, 0],
    '1': [0, 0, 0, 1],
    '2': [0, 0, 1, 0],
    '3': [0, 0, 1, 1],
    '4': [0, 1, 0, 0],
    '5': [0, 1, 0, 1],
    '6': [0, 1, 1, 0],
    '7': [0, 1, 1, 1],
    '8': [1, 0, 0, 0],
    '9': [1, 0, 0, 1],
    'A': [1, 0, 1, 0],
    'B': [1, 0, 1, 1],
    'C': [1, 1, 0, 0],
    'D': [1, 1, 0, 1],
    'E': [1, 1, 1, 0],
    'F': [1, 1, 1, 1],
}

# 앞쪽 0을 생략한 암호 코드
passcode_dict = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9,
}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 세로, 가로
    arr = [[] for _ in range(N)]  # 해독된 코드를 담을 arr

    # 각 줄을 입력 받으면서,
    for i in range(N):
        row_line = input()

        # 해당 줄을 2진수로 변환하여 arr에 담기(0이어도 변환)
        for j in range(M):
            # hex_to_bin을 이용하여, 각 글자를 2진수로 바꿔서 arr에 담기
            arr[i].extend(hex_to_bin[row_line[j]])

    ans = 0  # 정답을 저장할 변수

    # 입력 받은 코드를 위에서 아래로 보면서,
    for row_idx in range(N):
        idx = M * 4 - 1  # 마지막 인덱스
        # 왼쪽 끝(0)부터 56번째(55)까지만 마지막 코드의 가능성을 찾는다.
        while idx > 54:
            # arr[row_idx][idx] == 1 and arr[row_idx - 1][idx] == 0)
            # : 처음으로 암호코드를 만났다는 뜻
            # 즉, 처음으로 만난 암호코드만 검증하겠다는 뜻.
            if not (arr[row_idx][idx] == 1 and arr[row_idx - 1][idx] == 0):
                idx -= 1
                continue

            # 처음으로 암호코드를 만났다면
            password = []
            for _ in range(8):  # 암호코드는 8개의 숫자
                c2 = c3 = c4 = 0  # (0):1:0:1에서 1, 0, 1의 count
                # 이전 숫자의 (0)을 skip하기 위함
                while arr[row_idx][idx] == 0:
                    idx -= 1
                # 앞으로 가면서 0이 나올 때까지 1의 개수를 센다.
                while arr[row_idx][idx] == 1:
                    c4 += 1
                    idx -= 1
                # 앞으로 가면서 1이 나올 때까지 0의 개수를 센다.
                while arr[row_idx][idx] == 0:
                    c3 += 1
                    idx -= 1
                # 앞으로 가면서 0이 나올 때까지 1의 개수를 센다.
                while arr[row_idx][idx] == 1:
                    c2 += 1
                    idx -= 1
                # 위의 각각 while은 숫자가 0에서 1 혹은 1에서 0으로 바뀌는 시점에 종료 됨

                ratio = min(c2, c3, c4)  # c2, c3, c4 중 가장 작은 값으로 나눠서 비율을 만들어야만
                password.append(passcode_dict[(c2//ratio, c3//ratio, c4//ratio)])

            # 암호코드 검증하기
            even_sum = password[0] + password[2] + password[4] + password[6]
            odd_sum = password[1] + password[3] + password[5] + password[7]
            if (odd_sum * 3 + even_sum) % 10 == 0:
                ans += odd_sum + even_sum

            idx -= 1  # 암호코드를 해석했으면 앞으로

    print(f'#{tc} {ans}')