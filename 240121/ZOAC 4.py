h,w,n,m = map(int,input().split())

a,b = 0, 0
c = n+1
d = m+1
### 짝수면 몫으로 구하면 됨
if h % c ==0:
    a = h //c

elif h % c !=0:
    a = h//c +1

if w % d ==0 :
    b = w //d
elif w % d !=0:
    b = w//d+1

e = a * b
print(e)