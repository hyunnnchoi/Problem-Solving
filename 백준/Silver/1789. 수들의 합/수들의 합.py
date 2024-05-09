import sys
input = sys.stdin.readline

N = int(input())
accumulativeSum = 0
count = 0
for i in range(1, N):
    if accumulativeSum + i > N:
        break
    else:
        accumulativeSum += i
        count += 1

if N == 1:
    count = 1
print(count)