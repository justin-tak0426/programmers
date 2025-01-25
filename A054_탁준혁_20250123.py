def solution(board, moves):
    answer = 0
    stack = []
    
    for move in moves:            
        for row in board:
            if row[move-1] != 0:
                stack.append(row[move-1])
                row[move-1] = 0
                break
            else:
                pass
            
    print(stack)
    
    i=0
    while len(stack) >= 2:
        try:
            if stack[i] == stack[i+1]:
                del stack[i+1]
                del stack[i]
                answer += 2
                i -= 1
                continue
            i+=1
        except:
            print(len(stack), i)
            break
            
    
    return answer