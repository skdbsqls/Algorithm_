N, X = map(int, input().split())  # N일차, X일 동안
visit = list(map(int, input().split())) # N일 간 방문자수 배열

cur_sum = sum(visit[:X]) # 초기값
max_val = cur_sum # 최댓값
count = 1 # 최댓값 개수(cur_sum가 최댓값일 수 있기 때문에 1로 설정)

# 한 칸씩 이동하면서 앞에 하나 빼고 뒤에 하나 더하기
for i in range(X, N):
    cur_sum += visit[i] - visit[i - X]

    if cur_sum > max_val:
        max_val = cur_sum
        count = 1 # 진짜 최대값을 찾으면 그 때 1로 다시 초기화
    elif cur_sum == max_val:
        count += 1

if max_val == 0:
    print("SAD")
else:
    print(max_val)
    print(count)