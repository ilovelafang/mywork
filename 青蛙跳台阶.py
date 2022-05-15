
# 使用循环 时间复杂度O(n) 本质为斐波那契数列
def fibonacci2(n):
    if not isinstance(n, int):
        return '请输入整数'
    if n < 0:
        return '请输入正整数'
    if n == 1:
        return 1
    if n == 2:
        return 2
    fone = 1
    ftwo = 2
    fn = 0
    for i in range(3, n+1):
        fn = fone + ftwo
        fone = ftwo
        ftwo = fn
    return fn


if __name__ == '__main__':
    print('start')
    n = 10
    g = fibonacci2(n)
    print(g)
