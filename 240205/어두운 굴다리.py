import sys
import math

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
position = list(map(int, sys.stdin.readline().strip().split()))
result = position[0]
for i in range(1, M - 1):
    result = max(math.ceil((position[i] - position[i - 1]) / 2), result)
result = max(result, N - position[-1])
print(result)