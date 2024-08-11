import sys
import heapq
input = sys.stdin.readline

n = int(input())
line =  list(map(int,input().split()))
dp = [0] * n

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == line[i] and dp[j] == 0:
            dp[j] = i+1
            break
        elif dp[j] == 0:

            cnt +=1

for i in dp:
    print(i,end=" ")