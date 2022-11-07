N, K = map(int, input().split())
plug = list(map(int, input().split()))

now = []
cnt = 0

i = 0
while len(now) < N:
    if plug[i] not in now:
        now.append(plug[i])
    i += 1
    if i == len(plug):
        break

while i != len(plug):
    now_item = plug[i]
    if now_item not in now:                          # 이미 꽂혀있으면 패스
        cnt += 1                                     # 교체해야되니까 cnt + 1
        change = False                               # 교체했는지 확인하는 변수
        for j in range(len(now)):                    # 앞으로 쓸 일 없는 애로 교체하기
            if now[j] not in plug[i:]:
                now[j] = now_item
                change = True
                break
        if not change:                               # 교체 안됐으면
            check = [0]*len(now)                     # 꽂혀있는 애들중에
            for j in range(len(now)):                # 가장 나중에 쓸 애를 교체하기
                for z in range(i, len(plug)):
                    if now[j] == plug[z]:
                        check[j] = z
                        break
            now[check.index(max(check))] = now_item

    i += 1

print(cnt)