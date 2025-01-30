def solution(n):
    answer = fibo(n)
    
    return answer % 1234567

def fibo(n):
    if n==1:
        return 1
    if n==2:
        return 2
    
    fib = [0] * n
    fib[0] = 1
    fib[1] = 2
    
    for i in range(2, n):
        fib[i] = fib[i-2] + fib[i-1]
    
    return fib[n-1]
    
    