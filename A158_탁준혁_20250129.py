def solution(players, callings):  # 순위(num)는 list의 index와 동일한 방식으로 센다.
    # call to num, ctn으로 이름이 불린 선수의 순위를 조회할 것이다.
    ctn = {}

    # ctn에 모든 선수들의 현재 순위를 저장한다.
    for i in range(len(players)):
        ctn[players[i]] = i

    # 아래 for문의 i는 callings에서 이름이 불리는 선수다 (이하 winner).
    for i in callings:
        # winner의 새로운 순위
        winner_n = ctn[i]-1

        # winner에게 추월당한 선수(이하 loser)의 새로운 순위
        loser_n = ctn[i]

        # players에서 둘의 순위를 서로 바꾸고,
        players[winner_n], players[loser_n] = players[loser_n], players[winner_n]

        # ctn에 새로운 순위를 적용한다.
        ctn[players[winner_n]], ctn[players[loser_n]] = winner_n, loser_n

    return players