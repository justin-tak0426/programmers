def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    print(citations)
    num = 0
    for i in range(len(citations)):
        if citations[i] > num:
            num+=1
        else:
            break
    
    answer = num
    
    return answer