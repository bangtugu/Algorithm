# alp = 10
# cop = 10 
# problems = [[10,15,2,1,2],[20,20,3,3,4]]
# result = 15

alp = 0
cop = 0
problems = [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]
result = 13


def solution(alp, cop, problems):
    
    max_alp = 0
    max_cop = 0
    
    for i in range(len(problems)):
        problems[i][0] -= alp
        problems[i][1] -= cop

        if problems[i][0] < 0:
            problems[i][0] = 0
        if problems[i][1] < 0:
            problems[i][1] = 0

    for i in range(len(problems)):
        max_alp = max(max_alp, problems[i][0])
        max_cop = max(max_cop, problems[i][1])

    n = max_alp+1
    m = max_cop+1
    table = [[i+j for j in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            
            for problem in problems:

                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem

                if alp_req > i or cop_req > j: continue

                n_alp = min(max_alp, i+alp_rwd)
                n_cop = min(max_cop, j+cop_rwd)

                table[n_alp][n_cop] = min(table[n_alp][n_cop], table[i][j] + cost)

    
    return table[max_alp][max_cop]

print(solution(alp, cop, problems))