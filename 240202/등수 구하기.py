
N, score, P = map(int,input().split())



if N ==0:
    print(1)
else:
    board = list(map(int, input().split()))
    board.append(score)
    board.sort(reverse=True)

    a = board.index(score)

    if a >P:
        print(-1)
    else:
        if N == P and score == board[P]:
            print(-1)
        else:
            print(a+1)
