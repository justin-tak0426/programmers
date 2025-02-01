N = int(input())
names = [input()[0] for _ in range(N)]
first_letters = {}

for name in names:
   first_letters[name] = first_letters.get(name, 0) + 1

result = ''
for letter in sorted(first_letters.keys()):
   if first_letters[letter] >= 5:
       result += letter

print(result if result else 'PREDAJA')