from collections import deque
import heapq
import sys
from itertools import combinations
input = sys.stdin.readline

n,l,r = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    q = deque()
    union = []
    q.append((x,y))
    union.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx <n and 0 <=ny<n and visited[nx][ny] == False and l<=abs(A[x][y]-A[nx][ny])<=r:
                q.append((nx,ny))
                visited[nx][ny] = True
                union.append((nx,ny))
    return union
dong = 0
while True:
    visited = [[False] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                visited[i][j] = True
                num = bfs(i,j)
                if len(num) >1:
                    flag = True
                    people = sum(A[x][y] for x,y in num) // len(num)
                    for x,y in num:
                        A[x][y] = people
    if flag == False:
        print(dong)
        break
    dong +=1
