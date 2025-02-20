import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))

    my_queue = []  # 화덕
    i = 1  # 몇 번째 피자인가

    # 처음에 화덕의 크기 만큼 피자 넣기
    for _ in range(N):
        pizza = Ci.pop(0)  # 피자 꺼내서
        my_queue.append([pizza, i])  # 화덕에 넣기 [치즈의 양, 몇 번째 피자인지]
        i += 1

    # 하나의 피자가 남을 때까지
    while len(my_queue) != 1:
        # 1번 위치에 있는 피자의 치즈가 다 녹았다면,
        if my_queue[0][0] // 2 == 0:
            my_queue.pop(0)  # 화덕에서 꺼낸다.

            if Ci:  # 화덕에 넣어야 할 피자가 남았다면
                next_pizza = Ci.pop(0)  # 피자 꺼내서
                my_queue.append([next_pizza, i])  # 화덕에 넣는다.
                i += 1

        # 치즈가 다 녹지 않았다면,
        else:
            retry_pizza = my_queue.pop(0)
            retry_pizza[0] = retry_pizza[0] // 2  # 치즈의 양을 반으로 줄이고,
            my_queue.append(retry_pizza)  # 다 녹을 때까지 돌린다.

    # 남아 있는 피자가 몇 번째 피자인지 출력
    print(f'#{tc} {my_queue[0][1]}')