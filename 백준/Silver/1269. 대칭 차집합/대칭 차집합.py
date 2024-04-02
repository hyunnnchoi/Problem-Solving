# 대칭 차집합?

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

setAB = set(listA + listB)

print(2*len(setAB) - a - b)

#사실상 A, B 교집합을 전체에서 제거한 것.

#A, B 리스트 합친 뒤에, 거기서 listA의 개수 뺴면 되지 않나?
#set으로 A, B 갯수 센 다음,

#1,2,4 2,3,4,5,6
#set -> 123456
#A는 3개, B는 1개 ->
