def solution(arr):
    answer = [arr[0]]
    
    prev = arr[0]
    for i in arr[1:]:
        if prev == i:
            pass
        else:
            answer.append(i)
            prev = i
    
    return answer