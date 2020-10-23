# 方案1:暴力解法,暴力枚举法
def get_greatest_common_factor(a: int, b: int):
    big = max(a, b)
    small = min(a, b)
    if big % small == 0:
        return small
    for i in range(small // 2, 1, -1):
        if big % i == 0 and small % i == 0:
            return i


# 方案2:辗转相除法:两个正整数a,b(a>b),他们的最大公约数等于a除以b的余数c和b之间的最大公约数
def get_greatest_common_factor1(a: int, b: int):
    big = max(a, b)
    small = min(a, b)
    if big % small == 0:
        return small
    return get_greatest_common_factor(small, big % small)

# 方案3:更相减损法:两个正整数a,b(a>b),他们的最大公约数等于a-b的差c和b之间的最大公约数
def get_greatest_common_factor2(a: int, b: int):
    if a - b == 0:
        return a
    big = max(a,b)
    small = min(a,b)
    return get_greatest_common_factor(big - small,small)