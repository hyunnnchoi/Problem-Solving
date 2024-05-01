import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()
P = list([])
for i in range(2*N+1):
    if i%2 == 0:
        P.append('I')
    else:
        P.append('O')

P = ''.join(P)

C = 0
indexes = [i for i, c in enumerate(S) if c == 'I']
for i in indexes:
    if ''.join(S[i:i+2*N+1]) == P:
        C += 1

print(C)