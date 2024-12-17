import sys
input = sys.stdin.readline

N = int(input())
main = {}

for _ in range(N):
    temp = list(input().split())
    target = main
    for word in temp:
        target[word] = {}
        target = target[word]

temp = list(input().split())
answer = 'Impossible'
for word in temp:
    if word not in main: break
    if not main[word]:
        main.pop(word)
        continue
    next = list(main[word].keys())[0]
    main[next] = main[word][next]
    main.pop(word)
else:
    if not main:
        answer = 'Possible'
print(answer)