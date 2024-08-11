
import sys
input = sys.stdin.readline

n,k = map(int,input().split())

desk = list(input())

ans = 0
for i in range(n):
    if desk[i] ==  'P':
        for j in range(max(i-k,0),min(i+k+1,n+1)):
            if desk[j] == 'H':
                desk[j] = 0
                ans +=1
                break
print(ans)
