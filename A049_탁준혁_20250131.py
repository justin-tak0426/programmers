def is_vowel(c):
   return c in 'aeiou'

def check_password(password):
   # 조건 1: 모음 하나 포함
   if not any(is_vowel(c) for c in password):
       return False
       
   # 조건 2: 모음 3개 또는 자음 3개 연속 체크
   for i in range(len(password)-2):
       vowel_count = 0
       consonant_count = 0
       for j in range(3):
           if is_vowel(password[i+j]):
               vowel_count += 1
           else:
               consonant_count += 1
       if vowel_count == 3 or consonant_count == 3:
           return False
           
   # 조건 3: 같은 글자 연속 체크 (ee, oo 허용)
   for i in range(len(password)-1):
       if password[i] == password[i+1]:
           if password[i] not in 'eo':
               return False
               
   return True

while True:
   password = input()
   if password == 'end':
       break
   print(f'<{password}> is {"acceptable" if check_password(password) else "not acceptable"}.')