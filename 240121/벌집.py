

## 1(0) , 7(1), 19(2), 37(3), 61(4)

a = int(input())

n = 1
cnt = 1

while a > n:
    n += 6 *cnt  ### 6의 배수씩 더하기
    cnt +=1

print(cnt)

