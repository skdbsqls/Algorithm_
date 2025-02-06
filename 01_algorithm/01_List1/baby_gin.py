# 카운트 배열 만들기
num = int(input())
# [참고] 길이가 12인 이유는 마지막(9)에 대한 run을 조사할 때, 'IndexError'를 피하기 위함
c = [0] * 12  # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트

for i in range(6):
    c[num % 10] += 1
    num // 10

# Baby-Gin 구현하기
i = 0
tri = run = 0
while i < 10:  # 카드는 0부터 9까지 주어짐
    if c[i] >= 3:  # triplete 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue  # triplete이 두 번 있을 경우에 대비
    if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:  # run 조사 후 데이터 삭제
        c[i] -= 1
        c[i + 1] -= 1
        c[i + 2] -= 1
        run += 1
        continue  # run이 두 번 있을 경우에 대비
    i += 1

if run + tri == 2:
    print('Baby Gin')
else:
    print('Lose')
