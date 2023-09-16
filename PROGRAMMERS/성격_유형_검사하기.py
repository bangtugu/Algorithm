survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
result = "TCMA"

# survey = ["TR", "RT", "TR"]
# choices = [7, 1, 3]
# result = "RCJA"


def solution(survey, choices):
    
    d = {
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
        'A': 0,
        'N': 0
    }
    choice = [3, 2, 1, 0, -1, -2, -3]
    
    for i in range(len(survey)):
        d[survey[i][0]] += choice[choices[i]-1]
    
    k = list(d.keys())
    print(k)
    answer = ''
    for i in range(4):
        if d[k[i*2]] >= d[k[i*2+1]]:
            answer = answer + k[i*2]
        else:
            answer = answer + k[i*2+1]
        
    return answer


print(solution(survey, choices))