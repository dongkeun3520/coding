import sys
from itertools import combinations
input = sys.stdin.readline()
n,m = input().split()
n = int(n)
player = []
for _ in range(n):
    player.append(input())
player = set(player)
# print(player)
if m == 'Y':
    print(len(player))
elif m == 'F':
    answer = len(player) //2
    print(answer)
    # print(len(dong))
elif m =='O':
    answer = len(player) //3
    print(answer)
