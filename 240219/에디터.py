import sys
input = sys.stdin.readline

word = list(input().rstrip())
m = int(input())

left = word
right = []

for _ in range(m):

    a = list(input().rstrip().split())
    if a[0] == 'P':
        left.append(a[1])
    elif a[0] == 'L' and left:
        right.append(left.pop())
    elif a[0] == 'D' and right:
        left.append(right.pop())
    elif a[0] =='B' and left:
        left.pop()
b = left + right[::-1]
for b_ in b:
    print(b_,end="")