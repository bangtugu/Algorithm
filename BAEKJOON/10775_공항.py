import sys
input = sys.stdin.readline

G = int(input())
P = int(input())
cnt = list(range(G+1))
answer = 0
for i in range(1, P+1):
    now = int(input())
    if answer: continue

    temp_lst = [now]
    temp = now
    # cnt[temp] == temp인 경우 temp에 비행기를 대면 된다.
    # cnt[temp] != temp일 경우 cnt[temp]에 비행기를 대야 한다.
    while cnt[temp] != temp:
        # cnt[temp] == temp가 될 때 까지(자리가 비어있을때까지) temp를 cnt[temp]로 갱신한다.
        temp = cnt[temp]
        # 지금까지 확인한 자리를 저장해둔다. (한번에 갱신하기 위해서. 갱신하지 않으면 다음에 똑같은 루트로 탐색을 또 해야됨.)
        temp_lst.append(temp)
        # 0번 자리에 대야하는 경우 == 댈 수 없는 경우이므로 답을 저장하고 반복문에서 벗어난다.
        if temp == 0:
            answer = i-1
            break
    else:
        # (temp != 0 and temp == cnt[temp]인 경우) == temp번 자리에 비행기를 댄 경우
        # 지금까지 확인한 모든 자리에 다음 댈 자리를 temp-1로 갱신한다.
        for p in temp_lst:
            cnt[p] = temp-1

print(answer if answer else P)