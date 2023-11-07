n = int(input())

m = [0] * 100
m[0] = 0
m[1] = 1
for i in range(2, n + 1): #기억하자.. 
  m[i] = m[i - 1] + m[i - 2]
print(m[n])
