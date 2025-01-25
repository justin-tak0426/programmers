def solution(s):
    answer = True
    num_p = 0
    num_y = 0
    
    for c in s:
        if c=='p' or c=='P':
            num_p += 1
        elif c=='y' or c=='Y':
            num_y +=1
        else:
            pass

    return num_p == num_y