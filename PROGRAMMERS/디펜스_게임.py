# n = 7
# k = 3
# enemy = [4, 2, 4, 5, 3, 3, 1]

n = 2
k = 4
enemy = [3, 3, 3, 3]


'''
1
'''
# def solution(n, k, enemy):

#     i = 0
#     k_lst = [0] * k
#     now_min = 0

#     for j in range(k+1):
        
#         if j:
#             k_lst.sort()
#             now_max = k_lst.pop(-1)
#             n += now_max
        
#         while n >= 0:
#             if i >= len(enemy):
#                 return i

#             now_enemy = enemy[i]
#             if k_lst and now_min < now_enemy:
#                 k_lst[k_lst.index(now_min)] = now_enemy
#                 now_min = min(k_lst)

#             n -= now_enemy
#             i += 1

#     return i-1



'''
2
'''
# def solution(n, k, enemy):

#     i = 0

#     for j in range(k+1):
        
#         if j:
#             now_max = max(enemy[:i])
#             enemy[enemy.index(now_max)] = 0
#             n += now_max
        
#         while n >= 0:
#             if i >= len(enemy):
#                 return i

#             now_enemy = enemy[i]

#             n -= now_enemy
#             i += 1
            

#     return i-1

'''

진행된 라운드 중 enemy[i]의 수가 가장 클 때 무적권을 사용해야함.

1. k_lst에 가장 큰 enemy[i]값을 계속 갱신하면서 진행하다가 n이 0보다 작아졌을때, k_lst 에서 가장 큰 값을 다시 되돌려주며 k_lst의 길이를 하나씩 줄이는 방식

2. n이 0보다 작아졌을 때, 지금까지 막은 라운드에서 max, index를 활용 가장 큰 enemy[i]를 다시 돌려주고, 해당 enemy[i]는 0으로 바꾸는 방식

두 방법 다 4~5개의 TC에서 시간초과됨.

1 방식의 문제점 : k_lst 갱신마다 k_lst에 min, index 사용
                 k 사용시마다 k_lst에 sort, pop 사용.
                 k 값 커질수록 시간소모가 굉장히 커짐

2 방식의 문제점 : k 사용시마다 enemy에 max, index 사용
                 enemy 값, k값 커질수록 시간소모 커짐

enemy, k값의 상승에도 일정한 성능을 낼 수 있는 방법이 있을까?

'''

'''

검색해본 결과 heap을 사용해서 문제를 해결한다.

heap을 사용하면 값 삽입, 삭제 모두 O(logn)의 속도를 가지므로

1 : k_lst 갱신 : O(n) / k_lst 정렬 : O(nlogn) / k_lst 삭제 : O(1)
2 : 가장 큰 enemy[i] 탐색 및 삭제 : O(n)

3 : 지난 라운드 enemy[i] 저장 : O(logn) / k를 사용할 라운드 선택 및 삭제 : O(logn)

의 속도를 가지게 될 것 같다.

문제를 직접 풀지 못하고 검색해서 힌트를 얻었으니, 라이브러리를 사용하지 않고 구현해서 사용해봐야겠다.

'''

'''
3
'''
def solution(n, k, enemy):
    heap_lst = [0]

    
    def heapappend(n):
        heap_lst.append(n)
        now_index = len(heap_lst) - 1

        while now_index != 1:
            if heap_lst[now_index//2] < heap_lst[now_index]:
                heap_lst[now_index//2], heap_lst[now_index] = heap_lst[now_index], heap_lst[now_index//2]
                now_index = now_index//2
            else:
                return
        
        return

    
    def heappopmax():
        
        head = heap_lst[1]
        now_index = 1
        
        if len(heap_lst) == 2:
            return heap_lst.pop(1)

        heap_lst[1] = heap_lst.pop()

        while now_index < len(heap_lst):
            
            target_index = now_index
            child_1 = now_index*2
            child_2 = now_index*2+1

            if child_1 < len(heap_lst) and heap_lst[child_1] > heap_lst[target_index]:
                target_index = child_1
            if child_2 < len(heap_lst) and heap_lst[child_2] > heap_lst[target_index]:
                target_index = child_2
            
            if target_index == now_index:
                return head
            else:
                heap_lst[now_index], heap_lst[target_index] = heap_lst[target_index], heap_lst[now_index]
                now_index = target_index

        return head
    

    i = 0
    
    while i < len(enemy):

        now_enemy = enemy[i]

        n -= now_enemy
        heapappend(now_enemy)

        if n < 0:
            if k:
                now_k = heappopmax()
                n += now_k
                k -= 1
            else:
                return i

        i += 1
    
    return len(enemy)

print(solution(n, k, enemy))