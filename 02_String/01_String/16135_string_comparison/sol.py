import sys

sys.stdin = open('sample_input.txt')

# 풀이 1
T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    result = 0
    for i in range(len(str2) - len(str1) + 1):
        # i번째부터 존재를 확인할 단어(str1)의 길이 만큼 자르기
        word = str2[i: i + len(str1)]

        # 일치 하는지 비교하기
        if word == str1:
            result = 1
            break

    print(f'#{tc} {result}')


# 풀이 2-1
T = int(input())
for tc in range(1, T + 1):
    pattern = input()
    sentence = input()
    success = True

    # 0부터 pattern이 존재할 수 있는지 마지막 인덱스까지 하나씩 검사한다.
    for i in range(len(sentence) - len(pattern) + 1):
        # i부터 검사했을 때, 일치했는지를 확인할 플래그를 만든다.
        success = True

        for j in range(len(pattern)):
            # pattern의 j번째와 sentence의 i + j번째를 비교한다.
            if sentence[i + j] != pattern[j]:
                # 다르면 실패!
                success = False
                break

        # 앞의 for문이 정상 종료되면 성공, success는 True일 것이다.
        if success:
            # 그러면 나머지는 확인할 필요가 없다.
            # 문제의 요구사항이 존재 여부만 묻기 때문에.
            break

    if success:
        print(1)
    else:
        print(0)


# 풀이 2-2
T = int(input())
for tc in range(1, T + 1):
    pattern = input()
    sentence = input()
    success = False

    for i in range(len(sentence) - len(pattern) + 1):
        # for를 통해 패턴의 존재 여부를 확인한다.
        for j in range(len(pattern)):
            # 한 번이라도 다르면 for문이 중단되는데,
            if sentence[i + j] != pattern[j]:
                break
        # 중단되지 않았다는건 패턴을 찾았다는 뜻이다.
        else:
            # 플래그를 바꿔주고
            success = True
            break  # 나머지는 볼 필요 없다.

    if success:
        print(1)
    else:
        print(0)