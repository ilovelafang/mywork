import math


def get_binary(num: int):

    if not isinstance(num, int):
        return "请输入整数"

    value = []
    while num > 0:
        key = num % 2
        num = int(num / 2)
        value.append(key)
    print(value)
    print("".join(str(i) for i in value[::-1]))
    count = 0
    for i in value:
        if i == 1:
            count += 1
    print(count)
    return count


def get_binary2(n):
    count = 0
    while n:
        count += 1
        n &= n-1
    print(count)
    return count


if __name__ == '__main__':
    print('start')
    get_binary(9)
    get_binary2(9)
