import sys
sys.stdin = open('input.txt')


# 카드 두 장을 골라서 교환하는 함수
# rep: 몇 번째 교환인가(몇 번이나 더 교환을 해야 하는가)
def swap(rep):
    global max_prize

    # 다 교환했으면,
    if rep == n:
        prize = int(''.join(cards))  # 최종 상금으로
        max_prize = max(max_prize, prize)  # 최댓값 갱신
        return

    # 교환횟수가 남았으면,
    for i in range(len(cards)):  # 첫 번째 카드
        for j in range(i + 1, len(cards)):  # 두 번째 카드(앞서 고른 카드는 선택할 수 없음)

            cards[i], cards[j] = cards[j], cards[i]  # 교환하기

            # 만약, 같은 교환횟수에 똑같은 카드 배열이 없었다면,
            prize = int(''.join(cards))  # 카드 배열

            if prize not in memo[rep]:
                memo[rep].add(prize)  # 현재 카드 배열을 memo에 담아주고,
                swap(rep + 1)  # 다음 교체로 넘어감

            cards[i], cards[j] = cards[j], cards[i]  # 되돌리기


T = int(input())
for tc in range(1, T + 1):
    cards, n = input().split()
    cards = list(cards)  # 숫자판의 정보
    n = int(n)  # 교환 횟수

    max_prize = 0  # 최댓값
    # 교환 횟수당 등장한 카드 조합을 파악하기 위한 메모
    # i번째 set()은 i번 교환했을 때 등장했던 카드 배열의 집합
    memo = [set() for _ in range(n)]
    swap(0)

    print(f'#{tc} {max_prize}')