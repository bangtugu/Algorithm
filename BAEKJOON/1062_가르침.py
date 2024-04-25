import sys


input = sys.stdin.readline
base = set(['a', 'n', 't', 'i', 'c'])
N, K = map(int, input().split())


def isin(string, dict):
    if string in dict.keys(): return True
    return False


alp_dic = {'end' : 0}
for _ in range(N):
    
    word = input()
    temp = set()
    
    for alp in word[4:-4]:
        if alp in base: continue
        temp.add(alp)

    if temp:
        temp = sorted(list(temp))
        target = alp_dic
        for i in range(len(temp)):
            if not isin(temp[i], target): target[temp[i]] = {'end' : 0}
            target = target[temp[i]]
            if i == len(temp)-1:
                target['end'] += 1
    else:
        alp_dic['end'] += 1

if K < 5:
    print(0)
else:
    K -= 5

    def get_next(lst):
        sett = set(lst)
        next = set()
        
        idx = 0
        target = [alp_dic]
        while idx < len(target):

            for alp in lst:
                if alp in target[idx].keys():
                    target.append(target[idx][alp])
            
            idx += 1
        
        for dict in target:
            for alp in dict.keys():
                if alp == 'end' or alp in sett: continue
                next.add(alp)

        return sorted(list(next))


    def get_value(lst):
        
        idx = 0
        target = [alp_dic]
        while idx < len(target):

            for alp in lst:
                if alp in target[idx].keys():
                    target.append(target[idx][alp])
            
            idx += 1

        value = 0
        for dict in target:
            value += dict['end']
        
        return value


    def search(lst):        
        
        if len(lst) >= K: return get_value(lst)

        next = get_next(lst)
        if not next: return get_value(lst)

        for alp in next:
            if alp == 'end': continue
            if alp not in lst:
                value = search(lst+[alp])

        return value
        

    answer = search([])
    print(answer)