import sys
import heapq
input = sys.stdin.readline

N = int(input())
minusHeap = []
plusHeap = []

for _ in range(N):
    C = int(input())

    if C == 0:
        if len(minusHeap) == 0 and len(plusHeap) == 0:
            print(0)
        elif len(minusHeap) == 0:
            print(heapq.heappop(plusHeap))
        elif len(plusHeap) == 0:
            print(-heapq.heappop(minusHeap))
        else:
            if minusHeap[0] == plusHeap[0]: # 절댓값이 같다면
                print(-heapq.heappop(minusHeap))
            elif minusHeap[0] < plusHeap[0]: # 절댓값 작다면
                print(-heapq.heappop(minusHeap))
            else:
                print(heapq.heappop(plusHeap))


    else:
        if C < 0:
            heapq.heappush(minusHeap, -C)
        else:
            heapq.heappush(plusHeap, C)

