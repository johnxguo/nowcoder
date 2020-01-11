



if __name__ == "__main__":
    n = input()
    nums = list(map(int, input().split()))
    nums.sort()
    min_ = 201
    max_ = 0
    l = len(nums)
    for i in range(int(l / 2)):
        su = nums[i] + nums[l - i - 1]
        min_ = min(su, min_)
        max_ = max(su, max_)
    print(abs(min_ - max_))
