import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
cards = deque([i+1 for i in range(n)])
count = 0
while len(cards) != 1:
  if count % 2 == 0:
    del cards[0]
  else:
    cards.append(cards[0])
    del cards[0]
  count += 1

print(cards[0])