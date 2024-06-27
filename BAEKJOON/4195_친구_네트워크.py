import sys
input = sys.stdin.readline


T = int(input())

for tc in range(T):
    
    F = int(input())
    
    cnt = 0
    man_set = set()
    man_group = []
    man_idx = {}
    group_set_dic = {}

    for _ in range(F):
        a, b = input().split()
        for m in [a, b]:
            if m in man_set: continue
            man_set.add(m)
            man_idx[m] = cnt
            man_group.append(cnt)
            group_set_dic[cnt] = set([cnt])
            cnt += 1
        
        gs = [man_group[man_idx[a]], man_group[man_idx[b]]]
        tg = min(gs)

        for g in gs:
            if g == tg: continue
            for m in list(group_set_dic[g]):
                man_group[m] = tg
                group_set_dic[tg].add(m)

        print(len(group_set_dic[tg]))