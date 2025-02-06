import sys
input = sys.stdin.readline

N = int(input())

print('CY' if N%5 == 2 or not N%5 else 'SK')