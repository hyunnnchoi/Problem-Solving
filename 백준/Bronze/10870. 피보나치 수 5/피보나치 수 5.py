import sys
sys.setrecursionlimit(10**6)  

dic = {0:0, 1:1}

def Fib(n):
    if n in dic:
        return dic[n]

    dic[n] = Fib(n-1) + Fib(n-2)
    return dic[n]

n = int(input())
f = Fib(n)
print(Fib(n))