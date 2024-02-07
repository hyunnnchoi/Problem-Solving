n = int(input())
for _ in range(n):
  s = list(str(input()))
  stack = []
  tf = True
  for i in s:
    if i == '(':
      stack.append(i)
    else: # ')' 일 경우
      if len(stack) == 0: # 스택이 비어있다면 False
        tf = False
      else:  #아닐 경우 pop
        stack.pop()

  if len(stack) != 0: # 스택이 비어있지 않은 경우
    tf = False
  
  if tf == True:
    print("YES")
  else:
    print("NO")