import sys
input = sys.stdin.readline

n = int(input())

# stairs = [0] * 301
# for i in range( n ):
#     stairs[i] = int(input())
# dp = [0] * 301
stairs = [int(input()) for _ in range(n)]
dp = [[0] for _ in range(n)]

for i in range(n):
    if i == 0:
        dp[i] = stairs[i]
    elif i ==1:
        dp[i] = stairs[0] + stairs[i]
    elif i ==2:
        dp[i] = max(stairs[0] + stairs[i], stairs[1] + stairs[i])

    else:
        # dp[i] = max(dp[i-2]+stairs[i],dp[i-3]+stairs[i]+stairs[i-1])
        dp[i] = max((dp[i - 2] + stairs[i]), (dp[i - 3] + stairs[i] + stairs[i - 1]))
print(dp[n-1])

