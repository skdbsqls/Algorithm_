N, K = map(int, input().split())  # 원생의 수, 조의 개수
children = list(map(int, input().split()))  # 원생들의 키

difference = [0] * (N - 1)  # 앞뒤 원생의 키 차이 배열

# 키 차이 구하기 
for i in range(1, N):
    difference[i - 1] = children[i] - children[i - 1]

# 내림 차순 정렬(차이가 큰 것부터)
difference.sort(reverse=True)

result = 0  # 결과

# K조로 나눌거니까 K-1 개 만큼 차이가 큰 것은 빼고 나머지를 차이를 더함
for i in range(K - 1, len(difference)):
    result += difference[i]

print(result)