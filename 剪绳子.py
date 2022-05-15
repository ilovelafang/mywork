
def get_max(length: int):
    if not isinstance(length, int):
        return "pleate input int"
    if length <= 0:
        return "pleate input bigger than 0"
    if length == 1:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2
    max_list = [0, 1, 2, 3]
    for i in range(4, length+1):
        max_num = 0
        for j in range(1, i):
            fn = max_list[j] * max_list[i-j]
            if max_num < fn:
                max_num = fn
        max_list.append(max_num)
    print(max_list)
    return max_list[length]


if __name__ == '__main__':
    a = get_max(7)
    print(a)
