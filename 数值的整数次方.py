
def get_exponent(base: float, exponent: int):
    if not isinstance(base, float):
        return "base should be float"
    if not isinstance(exponent, int):
        return "exponent should be int"
    if base == 0:
        return 0
    res = my_pow(base, exponent)
    return res


def my_pow(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    if exponent < 0:
        return 1/get_exponent(base, -exponent)
    res = 1
    while exponent:
        res *= base
        exponent -= 1
    if exponent & 1:
        res *= base
    return res


if __name__ == '__main__':
    print('start')
    a = get_exponent(2.0, -3)
    print(a)
