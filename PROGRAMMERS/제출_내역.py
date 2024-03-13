'''TC1'''
dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
result = [1, 4]
'''TC2'''
dice = [[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]]
result = [2]
'''TC3'''
dice = [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]
result = [1, 3]


TC = 3
dice = [[[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]], [[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]], [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]]
result = [[1, 4], [2], [1, 3]]


def solution(dice):
    
    N = len(dice)
    M = 6**(N//2)
    dice_lst = []


    def split_dice(n, lst):
        
        if sum(lst) == N//2:
            A = []
            for i in range(1, N):
                if lst[i]:
                    A.append(i)
            dice_lst.append(A)
            return
        
        if n >= N: return

        lst[n] = 1
        split_dice(n+1, lst)
        lst[n] = 0
        split_dice(n+1, lst)
    
    
    split_dice(1, [0]*N)


    def rolling(lst):
        num = []
        num.extend(dice[lst[0]])
        for i in range(1, len(lst)):
            new_num = []
            for j in range(6):
                for n in num:
                    new_num.append(n + dice[lst[i]][j])
            num = new_num
        return num

    
    answer = [0, [0]*(N//2)]
    for A in dice_lst:
        B = []
        for i in range(N):
            if i not in A: B.append(i)
        
        Anum = rolling(A)
        Bnum = rolling(B)
        Awin = Bwin = tie = 0

        Anum.sort()
        Bnum.sort()
        Aidx = Bidx = M-1
        while True:
            if Anum[Aidx] > Bnum[Bidx]:
                Awin += Bidx+1
                Aidx-=1
            elif Anum[Aidx] < Bnum[Bidx]:
                Bwin += Aidx+1
                Bidx-=1
            else:
                Atienum = Btienum = 0
                temp = Anum[Aidx]
                while True:
                    if Aidx >= 0 and Anum[Aidx] == temp:
                        Atienum += 1
                        Aidx -= 1
                    if Bidx >= 0 and Bnum[Bidx] == temp:
                        Btienum += 1
                        Bidx -= 1
                    if (Anum[Aidx] != temp and Bnum[Bidx] != temp) or (Aidx < 0 and Bidx < 0):
                        break
                tie += Atienum*Btienum
                Awin += Atienum*(Bidx+1)
                Bwin += Btienum*(Aidx+1)
                if Aidx < 0 : Aidx = 0
                if Bidx < 0 : Bidx = 0    

            if Aidx == 0 or Bidx == 0:
                break
            


        winner = [Awin, A] if Awin>Bwin else [Bwin, B]
        if winner[0] > answer[0]:
            answer = winner        

    for i in range(N//2):
        answer[1][i] += 1
    
    return answer[1]


for t in range(TC):
    answer = solution(dice[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))