
import sys
input = sys.stdin.readline
n = int(input())
# s = []  ## list 로 하면 메모리 초과 때문에 set 을 사용
s = set()
for _ in range(n):
    arr = list(input().split())

    if len(arr) ==1:
        if arr[0] == "all":
            s = set([i for i in range(1,21)])
        elif arr[0] == "empty":
            s = set()
    else:
        string = arr[0]
        num = int(arr[1])
        if string == "add":
            if num not in s:
                s.add(num)
        if string == "remove":
            if num in s:
                s.discard(num)
        if string == "check":
            if num in s:
                print("1")
            else:
                print("0")
        if string == "toggle":
            if num in s:
                s.discard(num)
            else:
                s.add(num)


