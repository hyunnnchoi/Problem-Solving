import sys
input = sys.stdin.readline
"""
구해야 하는 것: 몇 개의 제곱수를 더한게 그 값이 되는지
접근법 1: 
1. sqrt를 해본다. 바로 나오면 return 하고 끝.
2. 안될 경우, 하나 작은 수 sqrt. 
"""

n = int(input().rstrip())
dp = [0,1]

for i in range(2, n+1):
    min_value = 1e9
    j = 1

    while(j**2) <= i:
        min_value = min(min_value, dp[i-j**2])
        j += 1
    dp.append(min_value+1)
print(dp[n])