# {1, 2, 3}을 포함하는 모든 순열 생성하기
for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i1 != i2:
            for i3 in range(1, 4):
                if i1 != i3 and i2 != i3:
                    print(i1, i2, i3)
'''
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
'''

# arr = [2, 3, 7]을 가지고 모든 순열 생성하기
arr = [2, 3, 7]
for i1 in range(3):
    for i2 in range(3):
        if i1 != i2:
            for i3 in range(3):
                if i1 != i3 and i2 != i3:
                    print(arr[i1], arr[i2], arr[i3])
'''
2 3 7
2 7 3
3 2 7
3 7 2
7 2 3
7 3 2
'''