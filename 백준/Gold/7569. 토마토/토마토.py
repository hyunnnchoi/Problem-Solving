from collections import deque
def ripen():
  index_hnm = [(i,j,k,0) for i in range(h) for j in range(n) for k in range(m) if graph[i][j][k] == 1]
  return index_hnm
def bfs():
  queue = deque()
  if len(ripen()) == 0:
    return -1
  for i in ripen():
    queue.append((i))
  while queue:
    #print(queue.popleft())
    h0, n0, m0, count = queue.popleft()
    if 0 <= h0-1 < h and 0 <= n0 < n and 0 <= m0 < m and graph[h0-1][n0][m0] == 0:
      graph[h0-1][n0][m0] = 1
      queue.append((h0-1, n0, m0, count+1))
    if 0 <= h0+1 < h and 0 <= n0 < n and 0 <= m0 < m and graph[h0+1][n0][m0] == 0:
      graph[h0+1][n0][m0] = 1
      queue.append((h0+1, n0, m0, count+1))
    if 0 <= h0 < h and 0 <= n0-1 < n and 0 <= m0 < m and graph[h0][n0-1][m0] == 0:
      graph[h0][n0-1][m0] = 1
      queue.append((h0, n0-1, m0, count+1))
    if 0 <= h0 < h and 0 <= n0+1 < n and 0 <= m0 < m and graph[h0][n0+1][m0] == 0:
      graph[h0][n0+1][m0] = 1
      queue.append((h0, n0+1, m0, count+1))
    if 0 <= h0 < h and 0 <= n0 < n and 0 <= m0-1 < m and graph[h0][n0][m0-1] == 0:
      graph[h0][n0][m0-1] = 1
      queue.append((h0, n0, m0-1, count+1))
    if 0 <= h0 < h and 0 <= n0 < n and 0 <= m0+1 < m and graph[h0][n0][m0+1] == 0:
      graph[h0][n0][m0+1] = 1
      queue.append((h0, n0, m0+1, count+1))
  return count

  
m, n, h = map(int, input().split())
graph = [[] * n for _ in range(h)]
for i in range(h):
    for _ in range(n):
        graph[i].append(list(map(int, input().split())))

temp = bfs()
if any(0 in a in b for b in graph for a in b):
    print("-1")
else:
    print(temp)

