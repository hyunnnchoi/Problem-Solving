import sys
from itertools import combinations
n = int(sys.stdin.readline().rstrip())
#2*n의 직사각형을 1*2, 2*1의 타일로 채우는 방법
#n이 홀수면 1*2가 홀수개여야, n이 짝수면 1*2가 짝수개여야 함
#2*n이 중요한게 아니라, 짝수개와 홀수개로 나누는 방법이 중요한듯.
#n만큼의 공간을 1, 2로 나눠서 넣는게 중요함.
#combination?

#f(n) = f(n-1) + f(n-2)
#값이 1일 때, 1
#2일 때, 2
#3일 때, 3

dp = [0] * 1001
dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
  dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])