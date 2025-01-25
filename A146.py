import itertools

def solution(A,B):
    answer = 0
    
    """
    index_num = range(0,len(A))
    
    per_list = list(itertools.permutations(index_num, len(A)))
        
    sum_list = []
    j=0
    for per in per_list:
        per = list(per)

        sum=0
        j=0
        for i in per:
            sum += A[i]*B[j]
            j += 1
            
        sum_list.append(sum)
            
    answer = min(sum_list)
    """
    A.sort()
    B.sort(reverse=True)
    
    sum = 0
    for i in range(len(A)):
        sum += A[i]*B[i]
        
    
    
    return sum