T = int(input())
for _ in range(T):
  n = int(input())
  #정수 n을 1,2,3의 합으로 나타내는 방법...
  #3을 최대한 이용
  #n=1: 1
  #n=2: 2
  #n=3: 4
  #n=4: 31 13 22 211 121 112 1111 -> 7
  #n=5: 32 23 311 131 113 122 212 221 2111 1211 1121 1112 11111 -> 13
  #f(n) = f(n-1) + f(n-2) + f(n-3)
  list = [0] * 20
  list[0] = 0
  list[1] = 1
  list[2] = 2
  list[3] = 4
  for i in range(4,n+1):
    list[i] = list[i-1] + list[i-2] + list[i-3]
  print(list[n])