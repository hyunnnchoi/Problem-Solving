import sys
import itertools
input = sys.stdin.readline

def combination(N, M):
    # M 팩토리얼 나누기 N 팩토리얼 곱하기 M-N 팩토리얼
    return int(factorial(M) / (factorial(N) * factorial(M-N)))

def factorial(A):
    if A == 0 or A == 1:
        return 1
    else:
        return A * factorial(A-1)

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    l = []

    for i in range(0,m):
        l.append(i)
    #최초 생각: 그냥 mCn 하면 되는거 아닌가?
    answer = combination(n, m)
    print(answer)

