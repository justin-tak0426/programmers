def solution(a, b):
    answer = ''
    total = 0
    one = [1,3,5,7,8,10,12]
    two = [4, 6, 9, 11]
    
    for i in range(1, a+1):
        if i == a:
            total += b
            break
        if i in one:
            total += 31
        elif i in two:
            total += 30
        else:
            total += 29
    
    std = total%7
    if std==1:
        answer = 'FRI'
    elif std==2:
        answer = 'SAT'
    elif std==3:
        answer = 'SUN'
    elif std==4:
        answer = 'MON'
    elif std==5:
        answer = 'TUE'
    elif std==6:
        answer = 'WED'
    else:
        answer = 'THU'
    return answer