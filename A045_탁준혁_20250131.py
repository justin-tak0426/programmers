word = input().upper()
unique_letters = list(set(word))

cnt_list = []
for x in unique_letters:
   cnt = word.count(x)
   cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
   print('?')
else:
   max_index = cnt_list.index(max(cnt_list))
   print(unique_letters[max_index])