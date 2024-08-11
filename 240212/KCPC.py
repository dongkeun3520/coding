import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n,k,t,m = map(int,input().split())
    board = [[0] * (k+1) for _ in range(n+1)]
    count = [0] * (n+1)
    time = [0] * (n+1)

    for index in range(m):
        i,j,s = map(int,input().split())
        board[i][j] = max(board[i][j],s)
        count[i] +=1
        time[i] = index

    score = []

    for i in range(1,n+1):
        score.append([i,sum(board[i]),count[i],time[i]])
    score = sorted(score,key = lambda x : (-x[1],x[2],x[3]))

    # print(score)
    for i in range(n):
        if t == score[i][0]:
            print(i+1)





