def solution(a, b, n):
    answer = 0
    
    while n >= a:
        bot = (n//a) * b

        answer += bot
        bot = (n//a) * b
        rem = n%a
        n = bot + rem
    
    return answer