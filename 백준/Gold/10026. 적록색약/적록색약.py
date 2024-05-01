import sys
sys.setrecursionlimit(1000000)

n = int(input())
graph = []
for _ in range(n):
  graph.append(list(input()))
visited = [[False] * n for _ in range(n)]
#직감 상 bfs문제로 보임
#적록색약의 경우 G를 R로 바꿔주면 될 듯
rgb_cnt, rb_cnt = 0, 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
  visited[x][y] = True
  current_color = graph[x][y]

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if (0 <= nx < n) and (0 <= ny < n):
      if visited[nx][ny] == False:
        if graph[nx][ny] == current_color:
          dfs(nx, ny)

for i in range(n):
  for j in range(n):
    if visited[i][j] == False:
      dfs(i, j)
      rgb_cnt += 1

for i in range(n):
  for j in range(n):
    if graph[i][j] == 'G':
      graph[i][j] = 'R'
      
visited = [[False] * n for _ in range(n)]

for i in range(n):
  for j in range(n):
    if visited[i][j] == False:
      dfs(i, j)
      rb_cnt += 1

print(rgb_cnt, rb_cnt)
