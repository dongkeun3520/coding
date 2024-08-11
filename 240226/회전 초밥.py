from collections import deque
from itertools import combinations
import heapq
import sys
input = sys.stdin.readline

n,d,k,c = map(int,input().split())
belt = []
for _ in range(n):
    belt.append(int(input()))
belt = belt + belt
max = 0
for i in range(n):
    number = len(set(belt[i:i+k] + [c]))
    if max < number:
        max = number
print(max)