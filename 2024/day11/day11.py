import sys
#CAUTION, IF YOU USE THIS ONE FOR THE SECOND CHALLENGE YOU WILL OVERFLOW.
def blink(stones):
    # apply one blink according to rules.
    output = []
    for s in stones:
        if s == '0':
            output.append('1')
        elif len(s) % 2 == 0:
            mid = len(s)//2
            # split and drop leading zeros.
            a = s[:mid].lstrip('0') or '0'
            b = s[mid:].lstrip('0') or '0'
            output += [a, b]
        else:
            output.append(str(int(s)*2024))
    return output

def main():
    data = open('input.txt').read().split()
    stones = [str(int(x)) for x in data]

    for _ in range(25):
        stones = blink(stones)
    print(f"Number of Stones: {len(stones)}")

if __name__ == '__main__':
    main()
