from collections import deque
n, m, v = map(int,input().split())
node_dfs = [False] * n
node_bfs = [False] * n

graph = [[] for _ in range(n)]
dfs_list = []
bfs_list = []

for _ in range(m):
  start, end = map(int, input().split())
  graph[start-1].append(end-1)
  graph[end-1].append(start-1)
  

def dfs(x):
  node_dfs[x] = True
  dfs_list.append(x+1)
  for next in graph[x]:
    if node_dfs[next] == False:
      dfs(next)

def bfs(x):
  #방문한걸로 체크
  node_bfs[x] = True
  queue = deque([x])
  while queue:
    v = queue.popleft()
    bfs_list.append(v + 1)
    for next in graph[v]:
      if node_bfs[next] == False:
        queue.append(next)
        node_bfs[next] = True

for i in range(n):
  graph[i].sort() # 작은수가 먼저 나오도록

dfs(v-1)
bfs(v-1)

for i in range(len(dfs_list)):
  print(dfs_list[i], end = ' ')

print()
for i in range(len(bfs_list)):
  print(bfs_list[i], end = ' ')