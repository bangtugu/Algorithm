# commands = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]

commands = ["UPDATE 1 1 1", "UPDATE 1 2 2", "UPDATE 2 1 3", "UPDATE 2 2 4", "MERGE 1 1 1 2", "PRINT 1 2", "UNMERGE 1 1", "PRINT 1 2", "PRINT 1 1"]

# commands = ["UPDATE 1 1 A", "UPDATE 2 2 B", "UPDATE 3 3 C", "UPDATE 4 4 D", "MERGE 1 1 2 2", "MERGE 3 3 4 4", "MERGE 1 1 4 4", "UNMERGE 3 3", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3", "PRINT 4 4"]

# commands = ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]

# ['UPDATE', '1', '1', 'menu']
# ['UPDATE', 'korean', 'hansik']
# ['UPDATE', '1', '3', 'group']
# ['UNMERGE', '1', '4']
# ['PRINT', '1', '3']

# def solution(commands):

#     table = ['' for _ in range(2500)]
#     word_dic = {}

#     answer = []

#     for command in commands:
#         command = list(command.split(' '))

#         if command[0] == 'UPDATE':
#             if len(command) == 3:
#                 before = command[1]
#                 after = command[2]

#                 if before not in word_dic.keys(): continue

#                 before_lst = word_dic.pop(before)

#                 if after not in word_dic.keys():
#                     word_dic[after] = []

#                 for lst in before_lst:
#                     if type(lst) is list:
#                         for idx in lst:
#                             table[idx] = after
#                     else:
#                         table[lst] = after
                    
#                     word_dic[after].append(lst)
        
#             else:
#                 idx = (int(command[1]) - 1) * 50 + int(command[2]) - 1
#                 after = command[3]
                
#                 if after not in word_dic.keys():
#                     word_dic[after] = []
                    
#                 if table[idx]:
#                     before = table[idx]

#                     if idx in word_dic[before]:
#                         word_dic[before].remove(idx)
#                         word_dic[after].append(idx)
#                         table[idx] = after
#                     else:
#                         for i in range(len(word_dic[before])):
#                             if type(word_dic[before][i]) is list and idx in word_dic[before][i]:
#                                 lst = word_dic[before].pop(i)
#                                 word_dic[after].append(lst)
#                                 for tidx in lst:
#                                     table[tidx] = after
#                                 break

#                 else:
#                     word_dic[after].append(idx)
#                     table[idx] = after

#         elif command[0] == 'MERGE':
#             idx1 = (int(command[1]) - 1) * 50 + int(command[2]) - 1
#             idx2 = (int(command[3]) - 1) * 50 + int(command[4]) - 1
            
#             word1 = table[idx1]
#             word2 = table[idx2]

#             if word1:
#                 after = word1
#                 before = word2
#             else:
#                 after = word2
#                 before = ''
#                 idx1, idx2 = idx2, idx1

#             if not after: continue

#             if before:
#                 if idx2 in word_dic[before]:

#                     word_dic[before].remove(idx2)
#                     table[idx2] = after

#                     if idx1 in word_dic[after]:
#                         word_dic[after].remove(idx1)
#                         word_dic[after].append([idx1, idx2])
                        
#                     else:
#                         for i in range(len(word_dic[after])):
#                             if type(word_dic[after][i]) is list and idx1 in word_dic[after][i]:
#                                 word_dic[after][i].append(idx2)
                
#                 else:
#                     for i in range(len(word_dic[before])):
#                         if type(word_dic[before][i]) is list and idx2 in word_dic[before][i]:
#                             lst = word_dic[before].pop(i)
#                             for idx in lst:
#                                 table[idx] = after
                            
#                             if idx1 in word_dic[after]:
#                                 word_dic[after].remove(idx1)
#                                 lst.append(idx1)
#                                 word_dic[after].append(lst)
                            
#                             else:
#                                 for i in range(len(word_dic[after])):
#                                     if type(word_dic[after][i]) is list and idx1 in word_dic[after][i]:
#                                         word_dic[after][i].extend(lst)
                            
#             else:
#                 table[idx1] = after
#                 table[idx2] = after
#                 if idx1 in word_dic[after]:
#                     word_dic[after].remove(idx1)
#                     word_dic[after].append([idx1, idx2])
#                 else:
#                     for i in range(len(word_dic[after])):
#                         if type(word_dic[after][i]) is list and idx1 in word_dic[after][i]:
#                             word_dic[after][i].append(idx2)
#                             break

#         elif command[0] == 'UNMERGE':
#             idx = (int(command[1]) - 1) * 50 + int(command[2]) - 1
#             word = table[idx]

#             if not word: continue

#             for i in range(len(word_dic[word])):
#                 if type(word_dic[word][i]) is list and idx in word_dic[word][i]:
#                         lst = word_dic[word].pop(i)
#                         for midx in lst:
#                             table[midx] = ''
#                         table[idx] = word
#                         word_dic[word].append(idx)
#                         break

#         else:
#             idx = (int(command[1]) - 1) * 50 + int(command[2]) - 1

#             if table[idx]:
#                 answer.append(table[idx])
#             else:
#                 answer.append('EMPTY')

#     return answer


def solution(commands):

    table = ['' for _ in range(2500)]
    isgroup = [0] * 2500
    word_dic = {'GROUP': []}
    answer = []
    

    def UPDATE(y, x, word):
        idx = 50*y + x
        before = table[idx]

        if before == word: return
        
        if word not in word_dic.keys():
            word_dic[word] = []

        # 해당 셀이 병합 O
        if isgroup[idx]:
            for lst in word_dic['GROUP']:
                if idx in lst:
                    # 병합되어있는 모든 셀에 대해서
                    for tidx in lst:
                        # 값이 있다면 해당 dic에서 제거
                        if before:
                            word_dic[before].remove(tidx)
                        # 변경값 dic에 추가, table 변경
                        word_dic[word].append(tidx)
                        table[tidx] = word
        # 병합 X
        else:
            # 값이 있을 때 해당 dic에서 제거
            if before:
                word_dic[before].remove(idx)
            word_dic[word].append(idx)
            table[idx] = word
                
        return


    def WORDTOWORD(word1, word2):
        
        # 바꿀 단어가 없으면 return
        if word1 not in word_dic.keys() or len(word_dic[word1]) < 1: return
        if word1 == word2: return
        
        # 기존 dic에서 제거, table 단어 변경
        word1_lst = word_dic.pop(word1)
        for idx in word1_lst:
            table[idx] = word2

        # 변경 dic에 추가
        if word2 not in word_dic.keys():
            word_dic[word2] = []
        word_dic[word2].extend(word1_lst)
        

    def MERGE(y1, x1, y2, x2):
        idx1 = 50*y1 + x1
        idx2 = 50*y2 + x2
        idx1_lst = [idx1]
        idx2_lst = [idx2]
        word1 = table[idx1]
        word2 = table[idx2]

        if idx1 == idx2: return

        # 1번 셀 병합 O
        if isgroup[idx1]:
            for i in range(len(word_dic['GROUP'])):
                if idx1 in word_dic['GROUP'][i]:
                    # 2번 셀과 같은 셀이라면 return
                    if idx2 in word_dic['GROUP'][i]:
                        return
                    # 셀 리스트 저장
                    idx1_lst = word_dic['GROUP'].pop(i)
                    break
        
        # 2번 셀 병합 O
        if isgroup[idx2]:
            for i in range(len(word_dic['GROUP'])):
                if idx2 in word_dic['GROUP'][i]:
                    # 셀 리스트 저장
                    idx2_lst = word_dic['GROUP'].pop(i)
                    break
        
        # 1번 셀에 값이 있다면 dic에서 제거
        if word1:
            for idx in idx1_lst:
                word_dic[word1].remove(idx)
        
        # 2번 셀에 값이 있다면 dic에서 제거
        if word2:
            for idx in idx2_lst:
                word_dic[word2].remove(idx)
        
        # 한 리스트로 합치기
        idx1_lst.extend(idx2_lst)
        # 그룹 리스트에 추가
        word_dic['GROUP'].append(idx1_lst)
        # 그룹 여부 수정
        for idx in idx1_lst:
            isgroup[idx] = 1

        # 1번 셀에 값이 있었다면 1번 값으로 table 변경 및 dic 추가
        if word1:
            for idx in idx1_lst:
                table[idx] = word1
            word_dic[word1].extend(idx1_lst)
        # 1번에 값이 없고 2번에 있었다면 ~~
        elif word2:
            for idx in idx1_lst:
                table[idx] = word2
            word_dic[word2].extend(idx1_lst)
        
        # 둘다 값이 없었으면 그룹 정보만 저장되고 끝


    def UNMERGE(y, x):
        idx = 50*y + x
        
        # 병합 안돼있으면 그냥 return
        if not isgroup[idx]: return
        
        word = table[idx]

        for i in range(len(word_dic['GROUP'])):
            if idx in word_dic['GROUP'][i]:
                lst = word_dic['GROUP'].pop(i)
                # 값이 있다면 모든 셀 값, 그룹 여부, dic에서 초기화, 지정 셀만 값 추가
                if word:
                    for tidx in lst:
                        table[tidx] = ''
                        isgroup[tidx] = 0
                        word_dic[word].remove(tidx)
                    table[idx] = word
                    word_dic[word].append(idx)
                # 값이 없다면 그룹 정보만 초기화
                else:
                    for tidx in lst:
                        isgroup[tidx] = 0
                return


    for command in commands:
        
        command = list(command.split(' '))
        com, value = command[0], command[1:]

        if com == 'UPDATE':
            if len(command) == 3:
                WORDTOWORD(value[0], value[1])
        
            else:
                UPDATE(int(value[0]) - 1, int(value[1]) - 1, value[2])

        elif com == 'MERGE':
            MERGE(int(value[0]) - 1, int(value[1]) - 1, int(value[2]) - 1, int(value[3]) - 1)

        elif com == 'UNMERGE':
            UNMERGE(int(value[0]) - 1, int(value[1]) - 1)

        else:
            idx = (int(value[0]) - 1) * 50 + int(value[1]) - 1

            answer.append(table[idx] if table[idx] else 'EMPTY')

    return answer


'''
4개 tc 런타임 에러

병합되지 않은 똑같은 셀에 대해 병합을 시도했을 때 같은 셀 두개가 병합된 것으로 처리되는 오류가 있었다.
225번째 줄에 똑같은 셀을 병합 시도할 경우 무시하도록 해서 해결되었다.
'''

print(solution(commands))