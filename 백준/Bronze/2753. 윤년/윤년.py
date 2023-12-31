import sys
input = sys.stdin.readline

n = int(input())
#4의 배수, 100의 배수 x
#혹은 400의 배수

if n%400 == 0:
  print(1)
elif n%4 == 0 and n%100 != 0:
  print(1)
else:
  print(0)