import sys
input = sys.stdin.readline


def change(num):
    if switch_list[num] == 0:
        switch_list[num] = 1
    else:
        switch_list[num] = 0

    return


switch = int(input())
switch_list = [-1] + list(map(int,input().split()))

number = int(input())
for _ in range(number):
    sex, num = map(int,input().split())

    if sex ==1:
        for i in range(1,len(switch_list)):
            if i % num == 0:
                change(i)
    if sex == 2:
        change(num)
        for i in range(switch//2):
            if num + i > switch or num - i <1 : break
            if switch_list[num-i] == switch_list[num+i]:
                change(num-i)
                change(num+i)
            else:
                break
# print(switch_list)

for i in range(1,len(switch_list)):
    print(switch_list[i], end = " ")
    if (i) % 20 ==0:
        print()
