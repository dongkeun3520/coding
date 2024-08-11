from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = deque()

for i in range(N):
    q.append(i+1)

def dong(q):
    q.popleft()
    a = q.popleft()
    q.append(a)
    return q

while True:
    if len(q) ==1:
        print(q[0])
        break
    else:
        q = dong(q)
