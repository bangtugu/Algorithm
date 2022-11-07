def solution(nums):
    N = len(nums)

    phonekemon = {}

    for num in nums:
        if num in phonekemon.keys():
            phonekemon[num] = phonekemon[num] + 1
        else:
            phonekemon[num] = 1

    if len(phonekemon) < N // 2:
        return len(phonekemon)
    else:
        return N // 2