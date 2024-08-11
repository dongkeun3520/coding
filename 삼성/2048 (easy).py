from collections import deque
from itertools import combinations
import heapq
import sys
input = sys.stdin.readline

n = int(input())

pan = [list(map(int,input().split())) for _ in range(n)]

print(pan)

def left(board):
    for i in range(n):
        cursor = 0
        for j in range(1,n):
            if board[i][j] !=0:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][cursor] == 0:
                    board[i][cursor] = tmp
                elif board[i][cursor] == tmp:
                    board[i][cursor] *=2
                    cursor +=1
                else:
                    cursor+=1
                    board[i][cursor] = tmp
    return board

def right(board):
    for i in range(n):
        cursor = n-1
        for j in range(n-1,-1,-1):
            if board[i][j] !=0:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][cursor] == 0:
                    board[i][cursor] = tmp
                elif board[i][cursor] == tmp:
                    board[i][cursor] *=2
                    cursor -=1
                else:
                    cursor -=1
                    board[i][cursor] = tmp
    return board