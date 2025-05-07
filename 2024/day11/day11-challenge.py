import sys
from collections import Counter

def blink_counts(stones):
    # given Counter of stone->count, return new Counter after one blink
    out = Counter()
    for s, cnt in stones.items():
        if s == '0':
            out['1'] += cnt
        elif len(s) % 2 == 0:
            mid = len(s)//2
            a = s[:mid].lstrip('0') or '0'
            b = s[mid:].lstrip('0') or '0'
            out[a] += cnt
            out[b] += cnt
        else:
            out[str(int(s)*2024)] += cnt
    return out


def main():
    data = open('input.txt').read().split()
    stones = Counter(str(int(x)) for x in data)
    # blink 75 times
    for _ in range(75):
        stones = blink_counts(stones)
    print(f"Number of Stones: {sum(stones.values())}")

if __name__ == '__main__':
    main()
