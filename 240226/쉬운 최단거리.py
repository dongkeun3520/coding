import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
dx, dy = [0,0,-1,1], [-1,1,0,0]

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 0
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx,ny = dx[i] +x, dy[i] + y
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 0
                elif graph[nx][ny] ==1:
                    visited[nx][ny] = visited[x][y]+1
                    queue.append((nx,ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 and visited[i][j]==-1:
            bfs(i,j)

# print(visited)

for i in range(n):
    for j in range(m):
        print(visited[i][j],end=' ')
        # if graph[i][j] == 0:
        #     print(0,end=' ')
        # else:
        #     print(visited[i][j],end=' ')
    print()

