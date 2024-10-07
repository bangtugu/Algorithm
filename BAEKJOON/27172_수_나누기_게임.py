import sys
input = sys.stdin.readline

N = int(input())
dic = {}
cards = list(map(int, input().split()))
maxnum = 0
for i in range(N):
    maxnum = max(maxnum, cards[i])
    dic[cards[i]] = i

answer = [0]*N
cards.sort()
for card in cards:
    for num in range(card*2, maxnum+1, card):
        if num in dic:
            answer[dic[num]] -= 1
            answer[dic[card]] += 1

print(*answer)