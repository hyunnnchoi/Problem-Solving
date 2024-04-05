import sys
import heapq
input = sys.stdin.readline

# 홀수번째마다 중앙값 출력
# Heapq 쓰는게 아닐지?

def insert(num):
    # 다 maxHeap에 때려넣고, minHeap과 길이 같게만 하면?
    # 뭐가 먼저 들어올지 모름...
    if len(minHeap) == len(maxHeap):
        heapq.heappush(minHeap, num)
    else:
        heapq.heappush(maxHeap, -num)

    if len(minHeap) > 0 and len(maxHeap) > 0 and minHeap[0] < -maxHeap[0]:
        temp = heapq.heappop(minHeap)
        heapq.heappush(maxHeap, -temp)
        heapq.heappush(minHeap, -heapq.heappop(maxHeap))

    # 2 0 1 1
    # 2 1
    # 3 1 -> 2 2
    # 3 2

T = int(input())
for _ in range(T):
    minHeap = []
    maxHeap = []
    resultList = []

    n = int(input())
    aList = []

    # n을 기준으로, 10으로 나눈 뒤 올림하여, 그만큼 입력받기
    for _ in range(0, n//10 + 1):
        temp = list(map(int, input().split()))
        aList += temp
    for i in range(0, n):
        insert(aList[i])
        if i%2 == 0:
            resultList.append(minHeap[0])
    l = len(resultList)
    print(l)
    for i in range(l):
        if (i+1) % 10 == 0:
            print(resultList[i])
        elif i == l-1:
            print(resultList[i])
        else:
            print(resultList[i], end = ' ')


#heapq를 두개 써서,
# 가장 큰 것과 가장 작은 것을 바꿔준다?
# 작은것만 저장하는 heap, 큰 것만 저장하는 heap 만들고,
# 큰 것중 가장 작은거 뽑으면? 그게 중앙값?