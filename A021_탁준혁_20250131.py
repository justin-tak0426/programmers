import sys

a = int( sys.stdin.readline().rstrip() )
n = 0
for i in range(a):
    b = int( sys.stdin.readline().rstrip() )
    n += b
print(n-(a-1))