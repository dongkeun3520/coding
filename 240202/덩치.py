
n = int(input())

weight = [list(map(int,input().split())) for _ in range(n)]


for i in range(n):
    cnt = 1
    for j in range(n):
        if weight[i][0]<weight[j][0] and weight[i][1] < weight[j][1]:
            cnt +=1
    print(cnt, end = " ")
