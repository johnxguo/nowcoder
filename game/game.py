

if __name__ == "__main__":
    hp = int(input())
    c1 = int(input())
    c2 = int(input())
    res = 0
    if c1 * 2 >= c2:
        res = int(hp / c1)
        if hp % c1 != 0:
            res += 1
    else:
        res = int(hp / c2) * 2
        mod = hp % c2
        if mod != 0:
            if mod <= c1:
                res += 1
            else:
                res += 2
    print(res)