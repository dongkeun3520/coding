import sys
input = sys.stdin.readline

N = int(input())
road = list(map(int,input().split()))

city = list(map(int,input().split()))
answer = 0
weight = city[0]
for i in range(len(road)):
    if i == 0:
        answer += city[i] * road[i]
        # print(answer)
    else:
        weight = min(weight,city[i])
        answer += weight * road[i]
        # print(answer)
print(answer)