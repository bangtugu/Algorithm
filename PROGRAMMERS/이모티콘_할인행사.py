users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]
result = [1, 5400]

# users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
# emoticons = [1300, 1500, 1600, 4900]
# result = [4, 13860]

'''
1. 가입자 최대한 늘리기
2. 가입자 최대한 늘린 상태에서 남은 user들에게 최대 판매액
'''
def solution(users, emoticons):

    sale_per = [10, 20, 30, 40]

    user_dic = {
        10 : [],
        20 : [],
        30 : [],
        40 : []
    }

    for [sale, cost] in users:
        if sale > 30:
            user_dic[40].append(cost)
        elif sale > 20:
            user_dic[30].append(cost)
        elif sale > 10:
            user_dic[20].append(cost)
        else:
            user_dic[10].append(cost)

    print(user_dic)
    
    el = len(emoticons)

    plus_user = 0
    income = 0

    for i in range(4**el):
        
        i_str = ''

        for _ in range(el-1):
            i_str = i_str + str(i%4)
            i = i//4

        i_str = i_str + str(i)

        e_price = {
            10: 0,
            20: 0,
            30: 0,
            40: 0
        }

        for j in range(el):
            if i_str[j] == '0':
                e_price[10] += emoticons[j] * 9 // 10
            elif i_str[j] == '1':
                e_price[20] += emoticons[j] * 8 // 10
            elif i_str[j] == '2':
                e_price[30] += emoticons[j] * 7 // 10
            else:
                e_price[40] += emoticons[j] * 6 // 10

        e_price[30] += e_price[40]
        e_price[20] += e_price[30]
        e_price[10] += e_price[20]
        
        n_pu = 0
        n_i = 0

        for sp in sale_per:
            for u_p in user_dic[sp]:
                if u_p <= e_price[sp]:
                    n_pu += 1
                else:
                    n_i += e_price[sp]

        if n_pu > plus_user:
            plus_user = n_pu
            income = n_i
        elif n_pu == plus_user:
            income = max(n_i, income)

    return [plus_user, income]

print(solution(users, emoticons))