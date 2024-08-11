

n = int(input())
body = []
for _ in range(n):
    body.append(input())


# print(body[1][2])


for i in range(n):
    if '*' in body[i]:
        h = i
        break

w = body[h].index('*')

print(h+1+1,w+1)
left = 0
for i in range(w):
    if '*' in body[h+1][i]:
        left +=1
right = 0
for i in range(w+1,n):
    if '*' in body[h+1][i]:
        right +=1

back = 0
for i in range(h+2,n):
    if '*' in body[i][w]:
        back +=1

left_leg = 0
for i in range(n):
    for j in range(w):
        if body[i][j] =='*' and body[i][j+1] =='_':
            left_leg +=1
right_leg = 0
for i in range(n):
    for j in range(w+1,n):
        if body[i][j-1] == '_' and body[i][j] == '*':
            right_leg +=1
print(left, right, back, left_leg,right_leg)


