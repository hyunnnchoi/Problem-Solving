n = int(input())
s = list(map(int, input().split()))

if(sum(s) > 0) :
  print("Right")
elif sum(s) == 0:
  print("Stay")
else:
  print("Left")