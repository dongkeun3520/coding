import sys
input = sys.stdin.readline


n = int(input())
dp = [-1] * 1000

dp[1] = 1
dp[2] = 0
dp[3] = 1

for i in range(4,n+1):
    if dp[i-1] ==1 or dp[i-3] ==1:
        dp[i] =0
    else:
        dp[i] = 1
if dp[n] == 1:
    print("SK")
else:
    print("CY")
#
# if n % 2 ==0:
#     print("CY")
# else:
#     print("SK")
# ### 1  2  3  4  5  6  7  8
# ### sk cy sk cy sk