dic = {0:0, 1:1}

n = int(input())
def Fib(n):
    if n in dic:
        return dic[n]

    dic[n] = Fib(n-1) + Fib(n-2)
    return dic[n]

print(Fib(n))