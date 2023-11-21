from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
  
for _ in range(t):
  visited = [0 for _ in range(10000)]
  a, b = map(int, input().split())
  
  queue = deque()
  queue.append((a,''))
  visited[a] = 1
  answer = ""
  
  while queue:
    
    a, c = queue.popleft()
    
    if a == b:
      answer = c
      break
      
    #D
    if 2*a <= 9999 and visited[2*a] == 0:
      visited[(2*a)] = 1
      queue.append([2*a, c + 'D'])
      
    if 2*a >= 10000 and visited[(2*a) % 10000] == 0:
      visited[((2*a) % 10000)] = 1
      queue.append([2*a % 10000, c + 'D'])
      
    #S
    if a - 1 < 0 and visited[9999] == 0:
      visited[9999] = 1
      queue.append([9999, c + 'S'])
      
    if a - 1 >= 0 and visited[a-1] == 0:
      visited[a-1] = 1
      queue.append([a-1, c + 'S'])
      
    #L
    L = int((a % 1000) * 10 + a / 1000)
    if visited[L] == 0:
      visited[L] = 1
      queue.append([L, c + 'L'])
      
    #R
    R = int((a % 10) * 1000 + a / 10)
    if visited[R] == 0:
      visited[R] = 1
      queue.append([R, c + 'R'])

  print(answer)