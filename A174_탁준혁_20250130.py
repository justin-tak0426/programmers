def solution(k, score):
    award = []  # 명예의 전당
    answer = []  # 매일 발표되는 최하위 점수
    
    for s in score:
        award.append(s)
        award.sort(reverse=True)  # 내림차순 정렬
        
        if len(award) > k:  # k명까지만 유지
            award.pop()
            
        answer.append(min(award))  # 현재 명예의 전당의 최하위 점수 기록
    
    return answer