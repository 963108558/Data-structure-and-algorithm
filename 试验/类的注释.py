def get_sum(a: int, b: int, c=10):
    """
    :param a: 第一个数字
    :param b: 第二个数字
    :return: 返回数字之和或乘积
    """
    try:
        return a + b + c
    finally:
        return a + b * c


result = get_sum(5, 6)


def get_add(y: int):
    return y % 3


lost_result = get_add(result)

print(lost_result)
