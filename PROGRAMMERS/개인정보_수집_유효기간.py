# today = "2022.05.19"
# terms = ["A 6", "B 12", "C 3"]
# privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
# result = [1, 3]


today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
result = [1, 4, 5]


def solution(today, terms, privacies):
    
    today_lst = list(map(int, today.split(".")))
    today_value = (today_lst[0] * 12 + today_lst[1]) * 28 + today_lst[2]

    term_dic = {}
    for term in terms:
        term_dic[term[0]] = int(term[1:])
    
    answer = []

    for i in range(len(privacies)):
        privacy = privacies[i]
        privacy_term = privacy[-1]
        privacy_lst = list(map(int, privacy[:-2].split(".")))
        
        privacy_value = (privacy_lst[0] * 12 + privacy_lst[1]) * 28 + privacy_lst[2]
        privacy_value += term_dic[privacy_term] * 28
        
        if today_value >= privacy_value:
            answer.append(i+1)
        
    return answer


print(solution(today, terms, privacies))