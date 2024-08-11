
n,m = map(int,input().split())
a = []

a = [list(map(int, input().split())) for _ in range(n)]
# for i in range(n):
#     score = list(map(int,input().split()))
#     a.append(score)

a.sort(key= lambda x :(-x[1],-x[2],-x[3]))
# a.sort(key = lambda x : (x[1], x[2], x[3]), reverse=True)

b = [a[i][0] for i in range(n)].index(m)


for i in range(n):
    if a[i][1:] == a[b][1:]:
        print(i+1)
        break
# print(medals)
# print(a)
# print(b)

# N, K = map(int, input().split())
#
# medals = [list(map(int, input().split())) for _ in range(N)]
#
# medals.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)
#
# idx = [medals[i][0] for i in range(N)].index(K)
#
# for i in range(N):
#     if medals[idx][1:] == medals[i][1:]:
#         print(i + 1)
#         break