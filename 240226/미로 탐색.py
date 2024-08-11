from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

graph = [list(map(int,input().rstrip())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    que = deque()
    que.append((x,y))
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <n and 0 <=ny<m and graph[nx][ny] ==1:
                que.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1


bfs(0,0)
print(graph[n-1][m-1])
# for i in range(n):
#     for j in range(m):
#         print(graph[i][j],end=' ')
#     print()



