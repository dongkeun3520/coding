import sys
input = sys.stdin.readline
n = int(input())
budget = list(map(int,input().split()))
total = int(input())
start,end = 0, max(budget)

while start<= end:
    mid= (end + start) //2
    answer = 0
    for i in budget:
        if i >= mid:
            answer += mid
        else:
            answer += i
    if answer <= total:
        start = mid+1
    else:
        end = mid - 1

print(end)
