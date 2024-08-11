import sys
input = sys.stdin.readline

n, m = map(int,input().split())

# memo = [input().rstrip() for _ in range(n)]
dong = {}
answer = 0
for _ in range(n):
    dong[input().rstrip()] = 1
    answer +=1
for i in range(m):
    blog = list(input().rstrip().split(','))
    for word in blog:
        if word in dong.keys():
            if dong[word] ==1:
                dong[word] =0
                answer -= 1
    # print(sum(dong.values()))
    print(answer)
