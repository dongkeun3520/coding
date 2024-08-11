from collections import deque
from itertools import combinations
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n,k = map(int,input().split())

distance = [INF]*100001

def dictra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))

    while q:
        dis,now = heapq.heappop(q)
        if dis > distance[now]:
            continue
        for a,b in [(now*2,dis),(now+1,dis+1),(now-1,dis+1)]:
            if 0 <= a <= 100000 and b < distance[a]  :
                distance[a] = b
                heapq.heappush(q,(b,a))

dictra(n)
print(distance[k])

#
# N, K = map(int, input().split())  # 시작 위치, 도착 위치
# distance = [INF]*100001  # 100001개의 떨어진 거리
#
# def dijkstra(start):  # 다익스트라
#     distance[start] = 0  # 시작 위치 초기화
#     q = []
#     heapq.heappush(q, (0, start))  # 시작 위치 우선 순위 큐 삽입
#
#     while q:
#         dis, now = heapq.heappop(q)
#         if dis > distance[now]:
#             continue
#         for a, b in [(now * 2, dis), (now + 1, dis + 1), (now - 1, dis + 1)]:
#             if 0 <= a <= 100000 and b < distance[a]:
#                 distance[a] = b
#                 heapq.heappush(q, (b, a))
#
# dijkstra(N)  # 시작 위치 다익스트라 실행
# print(distance[K])  # 시작 위치로부터 K가 떨어진 최소 거리