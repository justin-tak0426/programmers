def solution(x):
    x_str = str(x)
    sum = 0
    for i in x_str:
        sum += int(i)
    
    return x%sum==0