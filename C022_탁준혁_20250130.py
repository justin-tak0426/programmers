from itertools import combinations

def is_prime(n):
    # 소수 판별 함수
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    
    # 3개 숫자의 모든 조합 구하기
    for combo in combinations(nums, 3):
        # 합이 소수인지 확인
        if is_prime(sum(combo)):
            answer += 1
            
    return answer