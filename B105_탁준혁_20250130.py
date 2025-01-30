def solution(answers):
    # 각 수포자의 찍기 패턴
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 각 수포자별 정답 개수
    score = [0, 0, 0]
    
    # 각 문제별로 정답 체크
    for i, answer in enumerate(answers):
        if answer == pattern1[i % len(pattern1)]:
            score[0] += 1
        if answer == pattern2[i % len(pattern2)]:
            score[1] += 1
        if answer == pattern3[i % len(pattern3)]:
            score[2] += 1
    
    # 가장 높은 점수 찾기
    max_score = max(score)
    
    # 가장 높은 점수를 받은 사람들 찾기
    result = []
    for i in range(3):
        if score[i] == max_score:
            result.append(i + 1)
    
    return result