def solution(number, k):
    stack = [number[0]]
    
    index = 1
    while k!=0 and index < len(number):
        if len(stack) == 0:
            stack.append(number[index])
            index += 1
            continue
                    
        if stack[-1] < number[index]:
            element = stack.pop()
            k -= 1

            continue
        
        stack.append(number[index])

        index += 1
        
    for i in range(index, len(number)):
        stack.append(number[i])

    for i in range(k):
        stack.pop()

    answer = ""
    for i in stack:
        answer += i

    return answer