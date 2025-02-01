# 점수를 저장할 리스트
scores = []
max_score = 0  # 최고 점수
winner = 0     # 우승자 번호

# 5명의 참가자 점수 입력 받기
for i in range(5):
    # 각 참가자의 4개 점수를 입력받아 합계 저장
    participant_scores = list(map(int, input().split()))
    total_score = sum(participant_scores)
    scores.append(total_score)
    
    # 최고 점수와 우승자 갱신
    if total_score > max_score:
        max_score = total_score
        winner = i + 1  # 참가자 번호는 1부터 시작

# 우승자의 번호와 점수 출력
print(winner, max_score)