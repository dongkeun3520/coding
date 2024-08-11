import sys

input = sys.stdin.readline

n,m = map(int,input().split())

name = [list(input().split()) for _ in range(n)]
name = sorted(name,key= lambda x : int(x[1]))

for _ in range(m):
    score = int(input())
    left = 0
    right = n

    while left <= right:
        mid = (left + right) // 2
        if score <= int(name[mid][1]):
            result = mid
            right = mid -1
        else:
            left = mid +1

    print(name[result][0])





