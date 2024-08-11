from collections import deque
import heapq
from itertools import combinations
import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

result = 0
def dfs(x):
    global result
    if x == s:
        result = 1
        return
    if len(x) == 0:
        return
    if x[-1] == 'A':
        t = x[:-1]
        dfs(t)
    if x[0] == 'B':
        ss = x[1:][::-1]
        dfs(ss)
dfs(t)
print(result)
