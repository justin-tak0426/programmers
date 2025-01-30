def solution(arr):
    answer = arr[0]
    
    if(len(arr)==1):
        return answer
    else:
        for ix in range(1, len(arr)):
            answer = lcm(answer, arr[ix])

    return answer


def mul_element(a):
    mul_elem = list()
    
    if a==1:
        return [1]
    
    
    for i in range(1, int(a/2) + 1):
        if a%i == 0:
            mul_elem.append(i)
            mul_elem.append(int(a/i))
    
    mul_elem = list(set(mul_elem))
    mul_elem.sort()
        
    return mul_elem


def gcd(a, b):
    a = mul_element(a)
    b = mul_element(b)
    comm = list(set(a)&set(b))
    comm.sort()
    return comm[-1]


def lcm(a, b):
    return int(a*b / gcd(a, b))
    
    