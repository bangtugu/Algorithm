# numbers = [7, 42, 5]
# result = [1, 1, 0]

numbers = [63, 111, 95, 112, 1, 127, 128, 256]
result = [1, 1, 0, 1, 1, 1]

'''
1
'''
def solution1(numbers):
    # 문제에서 주어지는 가장 큰 수 10**15
    max_number = 10**15
    # 주어질 수 있는 가장 긴 이진수의 길이
    max_bi_number_len = 0
    while 2 ** max_bi_number_len < max_number:
        max_bi_number_len += 1
    
    # 가장 긴 이진수를 표현하는데에 필요한 이진트리의 노드 깊이
    max_node_depth = 0
    while 2 ** max_node_depth < max_bi_number_len:
        max_node_depth += 1
    
    # 주어질 수 있는 이진트리 길이 목록
    size_lst = [2**i-1 for i in range(max_node_depth)]
    # 각 노드들의 부모 노드 번호를 저장하는 리스트 
    parent_lst = [0] * 2**max_node_depth
    search_lst = [2**(max_node_depth-1), 0]
    temp = 2**(max_node_depth-2)
    i = 0

    # 모든 노드에 대해서 부모 노드 인덱스 저장 (루트 노드 제외)
    while i < len(search_lst):

        now = search_lst[i]

        if now == 0:
            temp //= 2
            if temp != 1:
                search_lst.append(0)

        parent_lst[now - temp] = now
        parent_lst[now + temp] = now

        if temp != 1:
            search_lst.extend([now - temp, now + temp])
        
        i += 1


    def can_trans(string):
        
        # 포화 이진트리는 depth(d)에 따라 2**d - 1개의 노드를 가지므로, 더미 노드를 추가하여 노드 갯수를 맞춰준다.
        while len(string) not in size_lst:
            string = '0' + string
        
        # 0번 인덱스에 더미 추가, 문제의 가정에 따라 중간값의 인덱스가 최상단 root임.
        string = '0' + string
        bi_len = len(string)
        root = bi_len//2
        
        # 코드에서 숫자를 이진트리로 변환하고 있지만
        # 문제 지문에서는 이진트리를 숫자로 표현하는 내용이었고
        # 이진트리에 더미노드를 추가할 때 루트 노드는 그대로 유지해야 하므로
        # 최상단 루트 노드는 더미일 수 없다.
        if string[root] == '0':
            return False

        # 모든 자식 노드들에 대해서
        for i in range(bi_len):
            # 최상단 노드는 제외
            if i == root: continue
            
            # 더미 자식 노드는 제외
            if string[i] == '0': continue

            # 하나의 이진트리로 표현되기 위해서는 최상단 루트를 제외한 모든 노드가 부모 노드를 가져야한다.
            if string[parent_lst[i]] == '1': continue

            # 여기까지 continue 되지 않았다면 부모 노드가 없는 노드 발견            
            return False
        
        # 최상단 root가 1이고
        # 최상단 노드 제외 모든 노드들이 더미가 아닌 부모 노드를 갖는다면
        return True
    

    answer = []
    
    for number in numbers:

        bi_num = ''
        while number > 1:
            bi_num = str(number % 2) + bi_num
            number //= 2
        bi_num = str(number) + bi_num

        # 이진수로 변환해서 함수로 넘겨주기

        if can_trans(bi_num):
            answer.append(1)
        else:
            answer.append(0)
        
    return answer


''' 
시간초과 5

주어지는 모든 수에 대해서
이진수 변환 -> 노드들의 부모노드 여부 확인
의 과정을 거치는데,
최대 10만개의 수가 주어질 수 있다.

함수 실행시 부모 노드값들을 정렬하는데에는 상대적으로 적은 시간이 소요되니까 손보지 않아도 될 것 같음.
부모노드 여부 확인 과정에 더 시간 절약을 하는 방향으로 개선을 해봐야되나?

이미 처리한 수들을 set에 저장해서
주어지는 수가 중복된 값이라면 바로 넘길 수 있게 할까 했지만,
어차피 중복되지 않는 10만개의 값을 주는 경우에 통과가 되지 않을테니 큰 의미가 없는 것 같다.

1인 자식노드 -> 0인 부모노드일때 return False 하는것과
0인 부모노드 -> 1인 자식노드일때 return False 하는것이 큰 차이가 있을까?
'''


'''
2
'''
def solution2(numbers):
    # 문제에서 주어지는 가장 큰 수 10**15
    max_number = 10**15
    # 주어질 수 있는 가장 긴 이진수의 길이
    max_bi_number_len = 0
    while 2 ** max_bi_number_len < max_number:
        max_bi_number_len += 1
    
    # 가장 긴 이진수를 표현하는데에 필요한 이진트리의 노드 깊이
    max_node_depth = 0
    while 2 ** max_node_depth < max_bi_number_len:
        max_node_depth += 1
    
    # 주어질 수 있는 이진트리 길이 목록
    size_lst = [2**i-1 for i in range(max_node_depth)]
    # 각 노드들의 자식 노드 번호를 저장하는 리스트 
    child_lst = [[] for _ in range(2**max_node_depth)]
    search_lst = [2**(max_node_depth-1), 0]
    temp = 2**(max_node_depth-2)
    i = 0

    # 모든 노드에 대해서 부모 노드 인덱스 저장 (루트 노드 제외)
    while i < len(search_lst):

        now = search_lst[i]

        if now == 0:
            temp //= 2
            if temp != 1:
                search_lst.append(0)

        child_lst[now] = [now - temp, now + temp]

        if temp != 1:
            search_lst.extend([now - temp, now + temp])
        
        i += 1


    def can_trans(string):
        
        # 포화 이진트리는 depth(d)에 따라 2**d - 1개의 노드를 가지므로, 더미 노드를 추가하여 노드 갯수를 맞춰준다.
        while len(string) not in size_lst:
            string = '0' + string
        
        # 0번 인덱스에 더미 추가, 문제의 가정에 따라 중간값의 인덱스가 최상단 root임.
        string = '0' + string
        bi_len = len(string)
        root = bi_len//2
        
        # 코드에서 숫자를 이진트리로 변환하고 있지만
        # 문제 지문에서는 이진트리를 숫자로 표현하는 내용이었고
        # 이진트리에 더미노드를 추가할 때 루트 노드는 그대로 유지해야 하므로
        # 최상단 루트 노드는 더미일 수 없다.
        if string[root] == '0':
            return False

        # 모든 짝수노드 (홀수는 최하단노드임)
        for j in range(2, bi_len, 2):
            if string[j] == '1': continue

            for child in child_lst[j]:
                if string[child] == '1':
                    return False
        
        # 최상단 root가 1이고
        # 최상단 노드 제외 모든 노드들이 더미가 아닌 부모 노드를 갖는다면
        return True
    

    answer = []
    
    for number in numbers:

        bi_num = ''
        while number > 1:
            bi_num = str(number % 2) + bi_num
            number //= 2
        bi_num = str(number) + bi_num

        # 이진수로 변환해서 함수로 넘겨주기

        if can_trans(bi_num):
            answer.append(1)
        else:
            answer.append(0)
        
    return answer


'''
그대로 시간초과 5
'''

'''
이진트리에서 리프 노드가 아닌 노드는 자신의 왼쪽 자식이 루트인 서브트리의 노드들보다 오른쪽에 있으며,
자신의 오른쪽 자식이 루트인 서브트리의 노드들보다 왼쪽에 있다고 가정합니다.

위의 조건을 통해, 루트를 기준으로 루트보다 작은(왼쪽) / 루트보다 큰(오른쪽) 이진트리로 쪼개나가는 재귀함수를 통해 더 간단하게 구현할 수 있었다.
'''


def solution3(numbers):

    
    def check(s, e, bi_str):

        if s == e:
            return bi_str[s]
        
        middle = (s+e)//2

        left = check(s, middle-1, bi_str)
        right = check(middle+1, e, bi_str)

        if left == False or right == False:
            return False

        if bi_str[middle] == '0' and (left == '1' or right == '1'):
            return False

        return bi_str[middle]


    answer = []

    for number in numbers:
        
        bi_num = ''
        while number > 1:
            bi_num = str(number % 2) + bi_num
            number //= 2
        bi_num = str(number) + bi_num

        tree_size = 1
        while tree_size < len(bi_num):
            tree_size = (tree_size+1) * 2 - 1
        
        bi_num = '0' * (tree_size - len(bi_num)) + bi_num

        if check(0, tree_size-1, bi_num) != False:
            answer.append(1)
        else:
            answer.append(0)

    return answer


'''
pass
'''


print(solution3(numbers))