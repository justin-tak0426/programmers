from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    
    ls = []
    count = 0
    
    queue = deque()
    for i in people:
        queue.append(i)
        
    while queue:
        #print("current queue: ",queue)
        if len(queue) > 1:
            mini = queue.popleft()
            maxi = queue.pop()
            #print("mini: {}, maxi: {}".format(mini,maxi))
            
            if mini+maxi <= limit:
                count += 1
            else:
                count += 1
                queue.appendleft(mini)
        else:
            queue.popleft()
            count +=1
        #print("count: ", count)
    
    return count