# 递归实现，时间复杂度较大,时间复杂度O(n2)
def fibonacci(n):
    if not isinstance(n, int):
        return '请输入整数'
    if n < 0:
        return '请输入正整数'
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)


# 使用循环 时间复杂度O(n)
def fibonacci2(n):
    if not isinstance(n, int):
        return '请输入整数'
    if n < 0:
        return '请输入正整数'
    if n == 1:
        return 0
    if n == 2:
        return 1
    fone = 0
    ftwo = 1
    fn = 0
    for i in range(3, n+1):
        fn = fone + ftwo
        fone = ftwo
        ftwo = fn
    return fn


if __name__ == '__main__':
    print('start')
    n = 10
    # k = fibonacci(n)
    # print(k)
    g = fibonacci2(n)
    print(g)
