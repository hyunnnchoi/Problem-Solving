from copy import deepcopy
o_li = ['0','1','2','3','4','5','6','6','7','8']
#print(num_li)
n = int(input())
n_li = list(str(n))
count = 1
for i in range(len(n_li)):
    if n_li[i] == '9':
        n_li[i] = '6'
        #print("changed")
    if n_li[i] in o_li:
        o_li.remove(n_li[i])
        #print("removed")
    else: #리스트에 없을 경우
        o_li += ['0','1','2','3','4','5','6','6','7','8']
        count += 1
        o_li.remove(n_li[i])
print(count)