n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

def get_count(li):
  new_dict = {}
  for i in li:
    if i in new_dict:
      new_dict[i] += 1
    else:
      new_dict[i] = 1
  return new_dict

new_dict = get_count(n_list)
new_list = [0] * m

for i in range(m):
  if m_list[i] in new_dict:
    new_list[i] = new_dict[m_list[i]]
    
print(*new_list)