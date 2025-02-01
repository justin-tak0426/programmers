scores = []
for i in range(8):
   scores.append((int(input()), i+1))

scores.sort(reverse=True)
top5 = scores[:5]

print(sum(score for score, _ in top5))
print(*sorted(index for _, index in top5))