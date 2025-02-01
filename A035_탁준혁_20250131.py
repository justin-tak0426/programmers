T = int(input())

for _ in range(T):
   expression = input().split()
   result = float(expression[0])
   
   for op in expression[1:]:
       if op == '@':
           result *= 3
       elif op == '%':
           result += 5
       elif op == '#':
           result -= 7
           
   print(f'{result:.2f}')