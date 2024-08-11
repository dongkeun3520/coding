from collections import deque
from itertools import combinations
import heapq
import sys
input = sys.stdin.readline

s = list(input().rstrip())
n = len(s)
a_cnt = s.count('a')
s = s + s
# print(s)
# print(s[5])
answer = 999999999999999
left = 0

for left in range(n):
  right = left + a_cnt
  # if right > len(s):
  #   temp = s[left:len(s)] + s[:right-len(s)]
  # else:
  #   temp = s[left:right]
  temp = s[left:right]
  # print(temp)
  answer = min(answer, temp.count('b'))
print(answer)


# s = input()
# a = s.count('a')
# # s += s[0:a-1]
# s = s
# min_val = float('inf')
# # for i in range(len(s)-(a-1)):
#
# for left in range(len(s)):
#     right = left + a
#     if right > len(s):
#         temp = s[left:len(s)] + s[:right-len(s)]
#     else:
#         temp = s[left:right]
#     min_val = min(temp.count('b'))
# print(min_val)