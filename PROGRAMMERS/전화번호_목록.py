def solution(phone_book):
    # 순서대로 (2시간초과)
    # for i in range(len(phone_book)):
    #     for phone in phone_book:
    #         if len(phone_book[i]) < len(phone):
    #             if phone_book[i] == phone[:len(phone_book[i])]:
    #                 return False

    # 길이 짧은거부터 (1시간초과)
    # for i in range(1,20):
    #     for num in phone_book:
    #         if len(num) == i:
    #             for target in phone_book:
    #                 if num == target:
    #                     pass
    #                 elif num == target[:len(num)]:
    #                     return False

    # 서로 한번씩만 비교 (2시간초과)
    # for i in range(len(phone_book)-1):
    #     for j in range(i+1, len(phone_book)):
    #         if len(phone_book[i]) < len(phone_book[j]):
    #             if phone_book[i] == phone_book[j][:len(phone_book[i])]:
    #                 return False
    #         elif len(phone_book[i]) > len(phone_book[j]):
    #             if phone_book[j] == phone_book[i][:len(phone_book[j])]:
    #                 return False

    phone_book.sort()                                                   # 문자열 정렬하면 포함하는 문자열이 앞에 위치하게 됨.
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False

    return True