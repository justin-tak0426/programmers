def get_divisors_count(n):
    count = 0
    # 제곱근까지만 검사
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            # i가 약수인 경우
            count += 1
            # n//i가 i와 다른 경우, 그것도 약수
            if i != n // i:
                count += 1
    return count

def solution(number, limit, power):
    iron_weights = []
    
    for i in range(1, number + 1):
        divisors_count = get_divisors_count(i)
        # 제한 수치를 초과하는 경우 power 값으로 대체
        iron_weights.append(power if divisors_count > limit else divisors_count)
    
    return sum(iron_weights)