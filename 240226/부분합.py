import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n,s = map(int,input().split())
numbers = list(map(int,input().split()))

left, right = 0,0
su = 0
answer = 100001
while right<n:
    if su >=s:
        su -= numbers[left]
        left +=1
        answer = min(answer,right-left+1)
    else:
      su += numbers[right]
      right +=1

if answer == 100001:
    print(0)
else:
    print(answer)
