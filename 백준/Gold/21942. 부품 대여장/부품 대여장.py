import sys
import datetime
input = sys.stdin.readline

dict = {}

N, L, F = input().split()
N = int(N)
F = int(F)
L_DDD, L_else = int(list(L.split('/'))[0]), list(L.split('/'))[1]
L_hh, L_mm = map(int, L_else.split(':'))
L = L_DDD * 24*60*60
L += L_hh*60*60
L += L_mm*60

failDict = {}
for _ in range(N):
    date, time, device, user = input().split()
    if (device, user) not in dict.keys():
        dict[(device, user)] = (date, time)
    else:
        yyyy, mm, dd = map(int, date.split('-'))
        hh,ss = map(int, time.split(':'))
        dA = datetime.datetime(yyyy, mm, dd, hh, ss)

        dateB, timeB = list(dict[(device, user)])[0], list(dict[(device, user)])[1]
        yyyB, mB, dB = map(int, dateB.split('-'))
        hB, sB = map(int, timeB.split(':'))
        dB = datetime.datetime(yyyB,mB,dB, hB,sB)

        delta = dA - dB

        penalty = int((delta.total_seconds()/60 - L/60) * F)
        if penalty > 0:
            if user in failDict.keys():
                failDict[user] = failDict[user] + penalty
            else:
                failDict[user] = penalty
        dict.pop((device, user))

        # 초 - 초,
if len(failDict) == 0:
    print(-1)
else:
    for i in sorted(failDict.keys()):
        print(i, failDict[i])

# 2 014/00:00 5
# 2021-02-03 23:14 transistor codethinking
# 2021-02-08 22:14 transistor codethinking


# 16 001/00:00 4000
# 2021-01-01 09:12 arduino tony9402
# 2021-12-31 13:24 arduino tony9402
# 2021-01-23 14:04 raspberrypi tony9402
# 2021-02-01 18:21 resistance amsminn
# 2021-02-03 23:14 transistor codethinking
# 2021-02-28 23:55 transistor codethinking
# 2021-02-09 12:45 resistance amsminn
# 2021-02-13 14:37 raspberrypi tony9402
# 2021-01-01 09:12 arduino tony9402
# 2021-01-13 13:24 arduino tony9402
# 2021-02-15 12:12 raspberrypi q540jh
# 2021-02-15 12:13 raspberrypi q540jh
# 2021-01-01 09:12 arduino tony9402
# 2021-01-01 09:13 monitor chansol
# 2021-01-01 09:18 arduino tony9402
# 2021-01-01 09:18 monitor chansol

