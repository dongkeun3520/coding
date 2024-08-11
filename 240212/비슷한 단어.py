import sys

input = sys.stdin.readline

n = int(input())

first = list(input())
answer = 0
for _ in range(n-1):
    word = list(input())
    cnt = 0
    for i in first:
        if i in word:
            word.remove(i)
        else:
            cnt +=1

    if cnt < 2 and len(word)< 2:
        answer +=1
print(answer)