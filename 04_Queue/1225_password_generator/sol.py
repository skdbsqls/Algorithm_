import sys

sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    nums = list(map(int, input().split()))

    i = 1  # 1 감소부터 시작
    # 마지막 요소가 0이면 프로그램 종료
    while nums[-1] != 0:
        # 감소는 1부터 5까지가 한 사이클
        if i > 5:
            i = 1
        temp = nums.pop(0)  # 맨 앞에 요소 꺼내서
        temp -= i  # 감소 시키기

        # 만약 감소 시킨 값이 0이거나 0보다 작아지는 경우
        if temp <= 0:
            temp = 0  # 0으로 유지

        nums.append(temp)  # 맨 뒤로 보내기

        i += 1  # i + 1

    # 출력
    print(f'#{tc} {" ".join(map(str, nums))}')