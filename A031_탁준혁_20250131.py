# 입력 받기
N, M = map(int, input().split())

# 필요한 최소 쪼개기 횟수 계산
# N×M개의 조각이 필요하므로, 쪼개기 횟수는 N×M-1
result = N * M - 1

# 결과 출력
print(result)