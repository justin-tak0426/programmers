n = int(input())
coords = []

for _ in range(n):
   x, y = map(int, input().split())
   coords.append((x, y))

coords.sort()

for x, y in coords:
   print(x, y)