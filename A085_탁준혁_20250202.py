def sum_digits(s):
   return sum(int(c) for c in s if c.isdigit())

n = int(input())
serials = []

for _ in range(n):
   serial = input()
   serials.append(serial)

serials.sort(key=lambda x: (len(x), sum_digits(x), x))

for serial in serials:
   print(serial)