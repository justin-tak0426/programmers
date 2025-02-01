s = input()
suffixes = []

for i in range(len(s)):
   suffixes.append(s[i:])

for suffix in sorted(suffixes):
   print(suffix)