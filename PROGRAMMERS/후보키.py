relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
result = 2


def solution(relation):
    
    possible = []


    def contain(pos, com):
        
        for po in pos:
            for num in po:
                if num not in com:
                    break
            else:
                return True
        return False


    def is_possible(comb):
        temp = set()
        for i in range(len(relation)):
            now = ''
            for idx in comb:
                now = now + str(relation[i][idx])
            if now in temp:
                return False
            temp.add(now)
        return True


    from itertools import combinations
    for i in range(1, len(relation[0])+1):
        for comb in combinations(range(len(relation[0])), i):
            if contain(possible, comb):
                continue
            if is_possible(comb):
                possible.append(comb)

    return len(possible)


print(solution(relation))