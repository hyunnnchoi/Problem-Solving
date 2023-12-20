import sys
import heapq
n = int(sys.stdin.readline().rstrip())
heap = []
for _ in range(n):
  i = int(sys.stdin.readline().rstrip())
  if i == 0 and len(heap) == 0:
    print(0)
  elif i == 0 and len(heap) != 0:
    print(heapq.heappop(heap))
  else:
    heapq.heappush(heap, i)