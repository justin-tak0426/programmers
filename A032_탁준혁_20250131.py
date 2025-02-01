# 테스트 케이스의 수 입력
T = int(input())

# 각 테스트 케이스에 대해 반복
for _ in range(T):
    # k(층)와 n(호) 입력
    k = int(input())
    n = int(input())
    
    # 아파트 생성 (k+1층, n호)
    apt = [[0] * (n+1) for _ in range(k+1)]
    
    # 0층 초기화 (1호부터 n호까지)
    for i in range(1, n+1):
        apt[0][i] = i
    
    # 1층부터 k층까지 각 호실의 거주민 수 계산
    for i in range(1, k+1):
        for j in range(1, n+1):
            apt[i][j] = sum(apt[i-1][1:j+1])
    
    # 결과 출력 (k층 n호의 거주민 수)
    print(apt[k][n])