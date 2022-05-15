import random


# 找出数组中的重复数字，并随机返回
def get_number(data: list) -> int:
    new_list = []
    tmp_list = []
    for i in data:
        if i in tmp_list:
            new_list.append(i)
        tmp_list.append(i)
    list_len = len(new_list)
    print(new_list)
    num = random.randint(0, list_len-1)
    print(num)
    return new_list[num]


if __name__ == '__main__':
    a = [1, 1, 3, 4, 5, 6, 7, 7, 8, 3, 9, 11, 12, 11, 9]
    b = get_number(a)
    print(b)
