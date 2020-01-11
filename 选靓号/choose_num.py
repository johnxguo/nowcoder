#https://www.nowcoder.com/test/question/005af31a10834b3688911463065ab47d?pid=16333343&tid=30182814

from collections import Counter

def dis(ct, k, st):
    if ct[st] >= k:
        return 0
    k -= ct[st]
    res = 0
    for i in range(1, 10):
        res, k = judgeDis(res, k, ct, i, st + i)
        if k <= 0:
            return res
        res, k = judgeDis(res, k, ct, i, st - i)
        if k <= 0:
            return res

def modify(nums, ct, k, st):
    if ct[st] >= k:
        return
    k -= ct[st]
    for i in range(1, 10):
        k = judgeModify(nums, k, st + i, st, range(len(nums)))
        if k == 0:
            return
        k = judgeModify(nums, k, st - i, st, range(len(nums) - 1, -1, -1))
        if k == 0:
            return

def judgeDis(res, k, ct, i, dt):
    if dt < 10 and dt >= 0:
        res += i * min(k, ct[dt])
        k -= ct[dt]
    return res, k

def judgeModify(nums, k, dt, st, rg):
    if dt < 10 and dt >= 0:
        for j in rg:
            if k == 0:
                break
            if nums[j] == dt:
                nums[j] = st
                k -= 1
    return k

def pros(n, k, nums):
    ct = Counter(nums)
    disi = -1
    mind = float('inf')
    for i in range(10):
        tmp = dis(ct, k, i)
        if tmp < mind:
            mind = tmp
            disi = i
    modify(nums, ct, k, disi)
    print(mind)
    print(''.join(map(str, nums)))


if __name__ == "__main__":
    n, k  = list(map(int, input().split()))
    nums = list(map(int, list(input().strip())))
    pros(n, k, nums)