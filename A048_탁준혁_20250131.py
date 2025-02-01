N = int(input())
group_word_count = 0

for _ in range(N):
   word = input()
   is_group_word = True
   used = []
   
   for i in range(len(word)):
       if word[i] not in used:
           used.append(word[i])
       elif word[i] != word[i-1]:
           is_group_word = False
           break
           
   if is_group_word:
       group_word_count += 1

print(group_word_count)