import sys

sys.stdin = open('input.txt')

for test_case in range(1, 11):
    C = int(input())
    box = list(map(int, input().split()))

    max_v = max(box)  # 최고점
    min_v = min(box)  # 최저점

    # 주어진 덤프 횟수 만큼 반복
    while C > 0:
        # 덤프 수행하기
        box[box.index(max_v)] -= 1  # 최고점에서
        box[box.index(min_v)] += 1  # 최저점으로 옮기기

        max_v = max(box)
        min_v = min(box)

        C -= 1  # 덤프 횟수 1회 차감

    result = max_v - min_v  # 결과

    print(f'#{test_case} {result}')