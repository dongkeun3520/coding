import sys
input = sys.stdin.readline

s = list(sys.stdin.readline().rstrip())

n = s.count('0')
m = s.count('1')

for _ in range(m//2):
    s.remove('1')

s = s[::-1]
for _ in range(n//2):
    s.remove('0')

for i in s[::-1]:
    print(i, end='')