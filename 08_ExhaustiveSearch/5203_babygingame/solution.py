import sys
sys.stdin = open('sample_input.txt')


# 정렬된 카드들을 확인하는 경우, idx를 기준으로 하면 잘못 판단될 수 있으니
# 카드의 개수를 받아서 판단하는 방식으로 진행하자.
def baby_gin(card_cnt):
    # 한 종류의 카드가 3개 이상이면, triplet
    for i in range(10):
        if card_cnt[i] > 2:
            return True

    # 어떤 카드가 1개 이상 있는데, 다음과 그 다음의 카드의 개수도 1개 이상이면, run
    for i in range(8):
        if card_cnt[i] and card_cnt[i + 1] and card_cnt[i + 2]:
            return True

    # 둘 다 아니면
    return False


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))  # 전체 카드

    # 각 플레이어가 가진 카드의 개수를 파악하는 리스트를 준비
    # 어떤 숫자 카드를 몇 장 가지고 있는지를 파악하는 리스트
    card_cnt1 = [0] * 10
    card_cnt2 = [0] * 10

    # 3장은 있어야 판단 가능(첫 두장은 일단 배분)
    for i in range(2):
        card_cnt1[cards[i * 2]] += 1
        card_cnt2[cards[i * 2 + 1]] += 1

    result = 0  # 결과
    # 나머지 카드를 순서대로 배분하면서, 승자를 판단
    for i in range(2, 6):
        card_cnt1[cards[i * 2]] += 1
        card_cnt2[cards[i * 2 + 1]] += 1

        if baby_gin(card_cnt1):
            result = 1
        elif baby_gin(card_cnt2):
            result = 2

        # 결과가 나왔으면 더 볼 필요가 없음
        if result:
            break

    print(f'#{tc} {result}')