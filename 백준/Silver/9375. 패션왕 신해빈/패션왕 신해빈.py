import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    outfit = {}
    for _ in range(n):
        temp = list(input().split())
        if temp[1] in outfit.keys():
            outfit[temp[1]] += 1
        else:
            outfit[temp[1]]  = 1
    # Values 값 다 곱하고, 1 뺌
    vals = outfit.values()
    #vals 가 1개인 경우? vals
    #vals가 2개인 경우? a b ab
    answer = 1
    if len(outfit) == 1:
        answer = list(outfit.values())[0]
    else:
        for i in vals:
            answer *= i+1
        answer -= 1
    print(answer)
