K, N = map(int, input().split())
lan_lines = [int(input()) for _ in range(K)]

lan_lines.sort()  # 오름차순 정렬
start, end = 1, max(lan_lines)  # 시작점, 끝점

while(start <= end):
    mid = (start + end) // 2
    cnt = 0  # 잘라진 랜선의 개수

    for line in lan_lines:
        cnt += line // mid

    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)