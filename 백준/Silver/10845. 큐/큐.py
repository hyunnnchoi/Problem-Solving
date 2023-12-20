import sys
from collections import deque

n = int(sys.stdin.readline())
list = deque()
while n>0:
  command = sys.stdin.readline().rstrip()
  #좌 우로 분리, 만약 단일 명령어일 경우?
  #push만 x를 받음.
  if "push" in command:
    command, num = command.split()
    num = int(num)
    list.append(num)
    n -= 1
  elif command == "pop":
    if len(list)==0:
      print(-1)
    else:
      print(list[0])
      list.popleft()
    n -= 1

  elif command == "size":
    print(len(list))
    n-=1

  elif command == "empty":
    print(1 if len(list)==0 else 0)
    n-=1

  elif command == "front":
    print(-1 if len(list)==0 else list[0])
    n-=1

  elif command == "back":
    print(-1 if len(list)==0 else list[-1])
    n-=1

  else:
    break

