'''TC1'''
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
result = [4, 1, 3, 0]


TC = 1
genres = [["classic", "pop", "classic", "classic", "pop"]]
plays = [[500, 600, 150, 800, 2500]]
result = [[4, 1, 3, 0]]


def solution(genres, plays):
    
    N = len(genres)

    genre_lst = []
    genre_idx = {}

    for i in range(N):
        if genres[i] not in genre_idx.keys():
            genre_idx[genres[i]] = len(genre_idx.keys())
            genre_lst.append([0, []])

        genre_lst[genre_idx[genres[i]]][0] += plays[i]
        genre_lst[genre_idx[genres[i]]][1].append([i, plays[i]])

    genre_lst.sort(key = lambda x: -x[0])

    answer = []
    for genre in genre_lst:
        genre[1].sort(key = lambda x: [-x[1], x[0]])
        for i in range(len(genre[1])):
            answer.append(genre[1][i][0])
            if i == 1: break

    return answer


for t in range(TC):
    answer = solution(genres[t], plays[t])
    correct = True if answer == result[t] else False
    comment = "answer = {}".format(result[t]) if correct else "answer = {} your are {}".format(result[t], answer)
    print("TC{} : {} {}".format(t+1, "PASS" if correct else "FAIL", comment))