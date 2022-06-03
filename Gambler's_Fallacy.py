import itertools
import random
from collections import Counter

NUM_COINS = 4
NUM_FLIPS = 1000

def new_sequence(event_counter):
    seq = ""
    for i in range(NUM_COINS):
        seq += coin_flip()
    event_counter[seq] += 1

def coin_flip():
    return "T" if random.random() < 0.5 else "H"

perms = ["".join(x) for x in list(itertools.product("TH", repeat=NUM_COINS))]
event_counter = {key: 0 for key in perms}
for i in range(NUM_FLIPS):
    new_sequence(event_counter)

for k, v in event_counter.items():
    proportion = str(round(v / NUM_FLIPS * 100, 2)) + "%"
    print(k, proportion)


# Sample Output: (The values change everytime you execute this code)
'''
TTTT 7.2%
TTTH 7.3%
TTHT 6.0%
TTHH 6.2%
THTT 5.2%
THTH 4.6%
THHT 7.3%
THHH 6.1%
HTTT 6.6%
HTTH 6.5%
HTHT 6.3%
HTHH 5.0%
HHTT 5.3%
HHTH 6.6%
HHHT 6.4%
HHHH 7.4%
'''