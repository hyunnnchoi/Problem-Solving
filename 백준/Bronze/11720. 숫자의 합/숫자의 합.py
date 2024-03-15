import sys

input = sys.stdin.readline

N = int(input().rstrip())

str = input().rstrip()
TEMP = list(map(int, str))

print(sum(TEMP))