import sys
input = sys.stdin.readline

N = int(input())
dic = {}
cards = list(map(int, input().split()))
for i in range(N):
    dic[cards[i]] = i

answer = [0]*N
cards.sort()
for i in range(N):
    for j in range(i+1, N):
        if not cards[j] % cards[i]:
            answer[dic[cards[i]]] += 1
            answer[dic[cards[j]]] -= 1

print(*answer)