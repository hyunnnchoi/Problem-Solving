import sys
input = sys.stdin.readline

n = int(input())
marathonerList = {}
for _ in range(n):
    marathoner = input().rstrip()
    if marathoner in marathonerList.keys():
        marathonerList[marathoner] += 1
    else:
        marathonerList[marathoner] = 1

for _ in range(n-1):
    marathoner = input().rstrip()
    if marathonerList[marathoner] > 1:
        marathonerList[marathoner] -= 1
    else:
        del marathonerList[marathoner]

#dict에 남은 것 출력
print(list(marathonerList.keys())[0])
# 검색과 삭제가 빠른 자료구조를 써야하는데, 중복을 허용해야 함. 그럼 뭐지? hashtable이 먼저 생각난다.r