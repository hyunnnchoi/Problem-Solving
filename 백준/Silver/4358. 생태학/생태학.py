#입력 사전 순,

import sys
input = sys.stdin.readline
DICT = {}

SUM = 0

for temp in sys.stdin:
    # temp = input()
    if (temp == "\n"):
        break
    else:
        SUM += 1
        line = temp.rstrip()
        if line in DICT:
            DICT[line] += 1
        else:
            DICT[line] = 1

DICT_SORTED = sorted(DICT.items())
for k, v in DICT_SORTED:
    v = v / SUM * 100
    print(k + " " + f"{v:.4f}")