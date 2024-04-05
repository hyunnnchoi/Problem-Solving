import sys
import heapq
input = sys.stdin.readline

n = int(input())
minHeap = []
maxHeap = []
def insert(num):
    if len(minHeap) == len(maxHeap):
        heapq.heappush(minHeap, num)
    else:
        heapq.heappush(maxHeap, -num)
    # maxHeap이 왼쪽, minHeap이 오른쪽
    # 짝수개 라면, 중간 두 수 중 작은 수 말하기.
    if len(minHeap) > 0 and len(maxHeap) > 0 and minHeap[0] < -maxHeap[0]:
        temp = heapq.heappop(minHeap)
        heapq.heappush(minHeap, -heapq.heappop(maxHeap))
        heapq.heappush(maxHeap, -temp)

for i in range(n):
    insert(int(input()))
    if i%2 == 0: # 홀수개인 경우
        print(minHeap[0])
    else:
        print(min(minHeap[0], -maxHeap[0]))