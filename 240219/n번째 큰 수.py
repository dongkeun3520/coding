import sys
import heapq
input = sys.stdin.readline

n = int(input())
dongkeun = []
for _ in range(n):
    array = list(map(int,input().split()))
    for i in range(n):
        if len(dongkeun)<n:
            heapq.heappush(dongkeun,array[i])
        else:
            if dongkeun[0] < array[i]:
                heapq.heappop(dongkeun)
                heapq.heappush(dongkeun,array[i])

print(dongkeun[0])