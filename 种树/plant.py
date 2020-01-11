#https://www.nowcoder.com/question/next?pid=16333343&qid=353473&tid=30182814
import sys

# 不设置这个，用递归会爆栈
sys.setrecursionlimit(5000)

def dfs(kindNums, last):
    m = sum(kindNums)
    maxk = max(kindNums)
    if maxk > int((m + 1) / 2):
        return 0
    if maxk > m / 2:
        index = kindNums.index(maxk) + 1
        if index == last:
            return 0
        else:
            kindNums[index - 1] -= 1
            ret = dfs(kindNums, index)
            if ret == 0:
                kindNums[index - 1] += 1
                return 0
            else:
                return [index] + ret
    for i in range(len(kindNums)):
        index = i + 1
        if index == last:
            continue
        if maxk == 0:
            return [1000]
        if kindNums[i] > 0:
            kindNums[i] -= 1
            ret = dfs(kindNums, index)
            if ret != 0:
                return [index] + ret
            else:
                kindNums[i] += 1
    return 0

def pros(n, kindNums):
    res = dfs(kindNums, 0)
    if res == 0:
        print('-')
    else:
        print(*res[:-1])

if __name__ == "__main__":
    n = int(input().strip())
    kindNums = list(map(int, input().split()))
    pros(n, kindNums)