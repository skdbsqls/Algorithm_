'''
DATA[i] <= 4 조건
'''

DATA = [0, 4, 1, 3, 1, 2, 4, 1]
COUNTS = [0] * 5  # 카운트 배열, max(DATA) + 1, 크기에 주의!
TEMP = [0] * len(DATA)  # 정렬된 배열

# 1. DATA에서 각 항목들의 발생 회수를 세고, 정수 항목들로 직접 인덱스 되는 카운트 배열 COUNTS에 저장
for i in range(len(DATA)):
    COUNTS[DATA[i]] += 1

print(COUNTS)  # [1, 3, 1, 1, 2]

# 2. 정렬된 집합에서 각 항목의 앞에 위치할 항목의 개수를 반영하기 위해 COUNTS의 원소를 조정
for i in range(1, 5):  # range(1, max(DATA) + 1)
    COUNTS[i] += COUNTS[i - 1]

print(COUNTS)  # [1, 4, 5, 6, 8]

# 3. DATA 원소들을 COUNTS 반영해 TEMP에 삽입한다.
for i in range(len(DATA) - 1, -1, -1):  # 뒤에서부터 정렬하는 이유: DATA 원소들의 기존 순서를 지키기 위함
    COUNTS[DATA[i]] -= 1  # DATA[i]까지의 개수 - 1 (인덱스)
    TEMP[COUNTS[DATA[i]]] = DATA[i]  # DATA[i]까지 차지한 칸 수 중 가장 오른쪽에 DATA[i] 기록

print(TEMP)  # [0, 1, 1, 1, 2, 3, 4, 4]
