import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 끝나는 시간을 기준으로 정렬하기
    arr.sort(key=lambda x: x[1])

    # 첫 번째 사용 신청은 확정!
    cnt = 1  # 이용할 수 있는 화물차의 수
    time = arr[0][1]  # 끝나는 시간

    # 그 다음 가능한 사용 신청 중 앞에 있는 빨리 끝나는 것으로 확정
    for start, end in arr:
        if start < time:  # 시작 시간이 앞의 끝나는 시간보다 빠르면 불가능
            continue
        time = end  # 끝나는 시간 갱신
        cnt += 1

    print(f'#{tc} {cnt}')