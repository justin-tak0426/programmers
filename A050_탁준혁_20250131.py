word = input()
result = ''

for c in word:
   # 각 문자를 3칸 앞으로 이동
   # ord('A')는 65, ord('Z')는 90
   num = ord(c) - 3
   if num < ord('A'):
       num += 26
   result += chr(num)

print(result)