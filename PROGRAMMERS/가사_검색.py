words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?", "fron?", "font?"]

'''
1
'''


def solution1(words, queries):
    answer = []
    words_dic = {}

    for word in words:
        w_l = len(word)
        if w_l in words_dic.keys():
            words_dic[w_l].append(word)
        else:
            words_dic[w_l] = [word]

    for querie in queries:
        q_l = len(querie)
    
        t_l = 0
        t_lst = []

        if q_l in  words_dic.keys():
            t_l = len(words_dic[q_l])
            t_lst = [1] * t_l

        '''
        1_1
        '''
        # for i in range(t_l):

        #     for j in range(q_l):
                
        #         if querie[j] != '?' and querie[j] != words_dic[q_l][i][j]:
        #             t_lst[i] = 0
        #             break

        '''
        1_2
        '''
        # for i in range(q_l):

        #     if querie[i] == '?':
        #         continue

        #     for j in range(t_l):

        #         if t_lst[j] and querie[i] != words_dic[q_l][j][i]:
        #             t_lst[j] = 0

        answer.append(sum(t_lst))
    
    return answer


'''
효율성 체크 5개 중 3개 시간초과


검색어 query들을 fr??? -> fro?? / fra??같은 부모 -> 자식 관계로 정리해서 검색어마다 새로 연산하지 않고 부모값을 참조하도록 해볼까?
'''


'''
2
'''


def solution2(words, queries):
    answer = []
    w_d = {}

    for word in words:
        w_l = len(word)
        if w_l in w_d.keys():
            w_d[w_l].append(word)
        else:
            w_d[w_l] = [word]

    q_d = {}
    
    for querie in queries:
        if querie not in q_d.keys():
            q_d[querie] = 0


    class querie_graph_dict:
        
        dic = {}


        # check_alp_number
        def can(self, w):
            numb = 0
            for a in w:
                if a != '?':
                    numb += 1
            
            return numb


        def create(self, g):
            self.dic[g] = [[g], []]


        def append(self, q):
            
            g = self.get_group(q)

            if g not in self.dic.keys():
                self.create(g)
                if q == g:
                    return
                
            self.dic[g][0].append(q)
            q_idx = self.get_idx(q)

            # now_n
            # now_check_lst
            # now_parent
            qn = self.can(q)
            ncl = [0]
            np_idx = 0
            npn = 1

            i = 0
            while i < len(ncl):
                t_idx = ncl[i]
                tn = self.can(self.dic[g][0][t_idx])

                if i == 0:
                    np_childs = self.get_childs(self.dic[g][0][0])
                    for child in np_childs:
                        ncl.append(self.get_idx(child))
                else:
                    if tn < qn and npn < tn and self.is_can_parent(self.dic[g][0][t_idx], q):
                        np_childs = self.get_childs(self.dic[g][0][t_idx])
                        for child in np_childs:
                            ncl.append(self.get_idx(child))
                        np_idx = t_idx
                        npn = tn

                i += 1

            self.dic[g][1].append([np_idx, q_idx])

            p_childs = self.get_childs(self.dic[g][0][np_idx])

            for child in p_childs:
                if qn < self.can(child) and self.is_can_parent(q, child):
                    c_idx = self.get_idx(child)
                    t_idx = self.dic[g][1].index([np_idx, c_idx])
                    self.dic[g][1][t_idx][0] = q_idx
            
            return

        def get_first_alp(self, q):
            fap = 0 if q[0] != '?' else -1
            return fap


        def get_group(self, q):
            fap = self.get_first_alp(q)
            group = '?' * (len(q)-1)
            group = q[fap] + group if fap == 0 else group + q[fap]

            return group


        def get_childs(self, q):
            g = self.get_group(q)

            qi = self.dic[g][0].index(q)
            
            childs = []
            relationships = self.dic[g][1]
            if relationships:
                for relationship in relationships:
                    if relationship[0] == qi:
                        childs.append(self.dic[g][0][relationship[1]])
            
            return childs


        def get_parent(self, q):
            fap = self.get_first_alp(q)
            g = self.get_group(q)

            qi = self.dic[g][0].index(q)
            for relationship in self.dic[g][1]:
                if relationship[1] == qi:
                    return relationship[0]
        

        def get_idx(self, q):
            g = self.get_group(q)
            idx = self.dic[g][0].index(q)

            return idx
        

        def is_can_parent(self, t, q):
            fap = self.get_first_alp(t)
            tn = self.can(t)
            if fap == 0:
                for i in range(tn):
                    if t[i] != q[i]:
                        return False
            else:
                for i in range(tn):
                    i += 1
                    i *= -1
                    if t[i] != q[i]:
                        return False
            return True


    #querie graph dict
    q_g_d = querie_graph_dict()

    for q in q_d.keys():

        q_g_d.append(q)

    q_g_d.calc()


    for querie in queries:
        answer.append(q_d[querie])

    return answer

'''
클래스로 한번 만들어보고싶어서 시작해봤다가 일만 커졌다.


1. 각 query마다 다 연산하지 말고, fro??의 경우 fr???의 값을 참조해서 최대한 문자열 비교를 적게 하도록 하기
2. 검색어가 중복될 경우 반복 진행하지 않도록 querie_dic 만들어서 나중에 answer에 한번에 append해서 return하기
3. ?는 query 앞이나 뒤에만 연속 배치되므로, query 길이 / ?의 앞뒤 위치에 따라 dp로 구현해봐야겠다.

'''


'''
3
'''
def solution3(words, queries):

    import sys
    sys.setrecursionlimit(11000)

    answer = []
    q_d = {}

    for word in words:
        first = '?' * len(word)
        if first in q_d.keys():
            q_d[first].append(word)
        else:
            q_d[first] = [word]
    
    
    def alp_count(qry):
        numb = 0
        for i in range(len(qry)):
            if qry[i] != '?':
                numb += 1
        
        return numb
    

    def query_dp(qry):

        if qry in q_d.keys():
            return q_d[qry]

        q_l = len(qry)
        n = alp_count(qry)

        temp = []

        if qry[0] != '?':
            for word in query_dp(qry[:n-1] + '?' * (q_l - n + 1)):
                if word[n-1] == qry[n-1]:
                    temp.append(word)

        else:
            for word in query_dp('?' * (q_l - n + 1) + qry[q_l - n + 1:]):
                if word[-n] == qry[-n]:
                    temp.append(word)
        
        q_d[qry] = temp

        return q_d[qry]


    for query in queries:
        if query not in q_d.keys():
            if '?' * len(query) in q_d.keys():
                query_dp(query)
            else:
                q_d[query] = []

    for query in queries:
        answer.append(len(q_d[query]))
    
    return answer

'''
효율성 테스트 5개 중 1번코드로 시간초과나던 3개는 통과가 됐는데 원래 통과되던 2개가 런타임 에러가 뜬다.

정확성 테스트에서 다 통과가 됐는데 왜 런타임 에러가 뜰까? 검색 키워드 길이가 1 이상 10000이하라서 길이 10000 가까이일때 재귀를 너무 들어가나?
재귀 제한을 넉넉하게 11000으로 설정해보니 런타임 에러는 해결됐지만 시간 초과가 났다.

?가 아닌 알파벳 갯수가 적은것부터 실행해서 중간 query들이 q_d에 저장되지 않도록 해볼까?

lambda를 사용해서 query.count('?') key로 queries를 정렬한 후 순서대로 실행해서 중간query 저장하지 않도록 해봐야겠다.
'''


'''
4
'''
def solution4(words, queries):

    import sys
    sys.setrecursionlimit(11000)

    answer = []
    q_d = {}

    for word in words:
        first = '?' * len(word)
        if first in q_d.keys():
            q_d[first].append(word)
        else:
            q_d[first] = [word]
    
    
    def alp_count(qry):
        numb = 0
        for i in range(len(qry)):
            if qry[i] != '?':
                numb += 1
        
        return numb
    

    def query_dp(qry):

        if qry in q_d.keys():
            return q_d[qry], alp_count(qry)

        q_l = len(qry)
        n = alp_count(qry)

        temp = []

        if qry[0] != '?':
            temp_query, temp_n = query_dp(qry[:n-1] + '?' * (q_l - n + 1))
            if qry not in queries:
                return temp_query, temp_n
            else:
                for word in temp_query:
                    if word[temp_n:n] == query[temp_n:n]:
                        temp.append(word)

        else:
            temp_query, temp_n = query_dp('?' * (q_l - n + 1) + qry[q_l - n + 1:])
            if qry not in queries:
                return temp_query, temp_n
            else:
                for word in temp_query:
                    if word[q_l - n : q_l - temp_n] == query[q_l - n : q_l - temp_n]:
                        temp.append(word)
        
        q_d[qry] = temp

        return q_d[qry], n

    sorted_queries = sorted(queries, key = lambda x : -x.count('?'))
    
    for query in sorted_queries:
        if '?' * len(query) in q_d.keys():
            query_dp(query)
        else:
            q_d[query] = []

    for query in queries:
        answer.append(len(q_d[query]))
    
    return answer


'''
오히려 시간초과 갯수가 3개로 늘었다.

검색해서 찾아보니 words를 trie 구조로 저장하고 탐색하는 방법이 있었다.

word의 각 알파벳을 key로 해서 깊게 들어가는 방식으로 저장해서, query의 각 알파벳으로 탐색해 들어가는 방식이다.
'''

def solution5(words, queries):
    words_trie = {}
    words_rev_trie = {}
    words_len_dict = {}


    def add(head, word):
        node = head
        for alp in word:
            if alp not in node.keys():
                node[alp] = {}
                node[alp]['len'] = []
            node = node[alp]
            node['len'].append(len(word))


    def search(head, query):
        node = head
        for alp in query:
            if alp == '?':
                return node['len'].count(len(query))
            elif alp not in node.keys():
                break
            node = node[alp]
        return 0


    for word in words:
        add(words_trie, word)
        add(words_rev_trie, word[::-1])
        word_len = len(word)
        if word_len not in words_len_dict:
            words_len_dict[word_len] = 0
        words_len_dict[word_len] += 1

    answer = []

    for query in queries:
        if query[-1] == '?':
            if query[0] == '?':
                answer.append(0 if len(query) not in words_len_dict.keys() else words_len_dict[len(query)])
            else:
                answer.append(search(words_trie, query))
        else:
            answer.append(search(words_rev_trie, query[::-1]))

    
    return answer


print(solution5(words, queries))


'''
통과

446번 줄에서 words_len_dict에 len(query)가 비어있으면 런타임 에러가 발생하는 문제가 있었다.
'''