def solution(n, lost, reserve):
    # 여벌이 있지만 도난당한 학생 처리
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    
    # 체육복 빌려주기
    for r in set_reserve:
        # 앞번호 학생에게 빌려주기
        if r-1 in set_lost:
            set_lost.remove(r-1)
        # 뒷번호 학생에게 빌려주기
        elif r+1 in set_lost:
            set_lost.remove(r+1)
    
    # 전체 학생 수에서 남은 도난 학생 수를 빼기
    return n - len(set_lost)