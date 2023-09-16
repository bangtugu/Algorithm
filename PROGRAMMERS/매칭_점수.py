word = 'blind'
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]

# word = 'Muzi'
# pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]

def solution(word, pages):
    
    
    def is_alp(alp):
        num = ord(alp)
        if 65 <= num <= 90 or 97 <= num <=122: 
            return True
        else:
            return False
        

    N = len(pages)    
    standard_scores = []
    urls = []
    connect_urls = []

    for i in range(N):
        ws = []
        score = 0
        w = ''
        url = ''
        curl = []
        for j in range(len(pages[i])):
            alp = pages[i][j]
            if is_alp(alp):
                w = w + alp
            else:
                if w:
                    ws.append(w)
                if len(w) == len(word) and w.upper() == word.upper():
                    score += 1
                if w == 'https':
                    url = 'https'
                w = ''

            if url:
                if alp != '"':
                    url = url + alp
                else:
                    is_url = True
                    for z in range(j, -1, -1):
                        if pages[i][z] == '<':
                            if pages[i][z+1] != 'a' and pages[i][z+1] !='m':
                                is_url = False
                            break
                    if is_url:                                              #페이지 url도(<meta>태그) 아니고 외부링크(<a>태그)도 아닌데 url 형식을 취하는 문구가 있을 경우 10번 tc에서 틀린다.
                        for z in range(len(ws)-1, -1, -1):
                            if ws[z] == 'a' and ws[z+1] == 'href':
                                curl.append(url)
                                break
                            if ws[z] == 'url':
                                urls.append(url)
                                break
                    url = ''
        connect_urls.append(curl)
        standard_scores.append(score)
    
    total_scores = [0] * N
    
    for i in range(N):
        score = standard_scores[i]
        url = urls[i]
        for j in range(N):
            if i == j: continue
            if url in connect_urls[j]:
                score += standard_scores[j] / len(connect_urls[j])
                
        total_scores[i] = score

    max_score = max(total_scores)
    for i in range(len(total_scores)):
        if total_scores[i] == max_score:
            return i
        

print(solution(word, pages))