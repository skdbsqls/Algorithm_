import sys
sys.stdin = open('input.txt')

# 중위순회 하기
def in_order(n, result):
    if n:
        result = in_order(left[n], result)  # 왼쪽 자식으로 이동
        result += chars[n]  # visit(n) 결과에 해당 문자 담아주기
        result = in_order(right[n], result)  # 오른쪽 자식으로 이동

    return result


for tc in range(1, 11):
    N = int(input())  # 정점의 수
    chars = [''] * (N + 1)  # 정점이 가지는 문자를 저장
    left = [0] * (N + 1)  # 부모 인덱스로 왼쪽 자식 저장
    right = [0] * (N + 1)  # 부모 인덱스로 오른쪽 자식 저장

    for _ in range(N):
        arr = input().split()
        p = int(arr[0])  # 정점
        char = arr[1]  # 정점이 가지는 문자

        # 정점이 가지는 문자 저장
        chars[p] = char
        # 정점이 가지는 왼쪽 자식 저장
        if len(arr) > 2 :
            left_c = int(arr[2])
            left[p] = left_c
        # 정점이 가지는 오른쪽 자식 저장
        if len(arr) > 3:
            right_c = int(arr[3])
            right[p] = right_c

    # 중위순회 하기
    root = 1  # 루트는 항상 1
    result = in_order(root, '')  # 결과

    # 출력
    print(f'#{tc} {result}')
