n = int(input())

for _ in range(n):
   quiz = input()
   score = 0
   combo = 0
   
   for result in quiz:
       if result == 'O':
           combo += 1
           score += combo
       else:
           combo = 0
           
   print(score)