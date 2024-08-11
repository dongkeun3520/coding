

## 자기 앞에 자기보다 키가 큰 학생이 없다면 그냥 그 자리에 서고 차례가 끝난다.
## 자기 앞에 자기보다 키가 큰 학생이 한 명 이상있다면 그중 가장 앞에 있는 학생의 바로 앞에 선다.
## 이때, A부터 그 뒤의 모든 학생들은 공간을 만들기 위해 한칸씩 뒤로 물러서게 된다.

#
# n = int(input())
#
# for i in range(n):
#     arr = list(map(int,input().split()))
#     line = [0]*21
#     line[0] = i
#     cnt = 0
#     line[1] = arr[1]
#     for j in range(2,21):
#         if arr[j] > max(line):
#             line[j] = arr[j]
#         else:
#             for k in range(len(line)-1):
#                 if line[k] < arr[j]:
#                     continue
#                     #### 900 901 903 904 <-- 9002
#                 else:
#                     for m in range(k,len(line)-1):
#                         line[m+1] = line[m]
#                         line[m] = arr[j]
#                         cnt +=1
#     print((i+1),cnt)
#     # answer = [str(i+1),str(cnt)]
#     # print(" ".join(answer))


P=int(input())
for _ in range(P):
    arr=list(map(int,input().split()))
    total=0
    for i in range(1,len(arr)-1):
        for j in range(i+1,len(arr)): # i 뒤에 애들과 전부 비교해서
            if arr[i] > arr[j]:  # i가 더 크면
                arr[i],arr[j] = arr[j],arr[i]  # 자리바꾸기
                total+=1
    print(arr[0], total)