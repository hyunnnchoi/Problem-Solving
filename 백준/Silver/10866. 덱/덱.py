#파이썬에서 최대 힙: heapq
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
list = deque()
for _ in range(n):
  command = sys.stdin.readline().rstrip()
  
  if 'push_back' in command:
    command, num = command.split()
    list.append(num)
    
  elif 'push_front' in command:
    command, num = command.split()
    list.appendleft(num)
    
  elif command == 'pop_front':
    if len(list) == 0:
      print(-1)
    else:
      print(list[0])
      list.popleft()
      
  elif command == 'pop_back':
    if len(list) == 0:
      print(-1)
    else:
      print(list[-1])
      list.pop()
      
  elif command == 'size':
    print(len(list))
    
  elif command == 'empty':
    print(0 if len(list) != 0 else 1)
    
  elif command == 'front':
    if len(list) == 0:
      print(-1)
    else:
      print(list[0])
      
  elif command == 'back':
    if len(list) == 0:
      print(-1)
    else:
      print(list[-1])
  else:
    continue