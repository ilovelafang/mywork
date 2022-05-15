# 二维有序数据，左到右一次增大，上到下依次增大
def search_value(data: list, value: int) -> bool:
    my_list = []
    for i in data:
        num = len(i)-1
        if i[0] <= value <= i[num]:
            my_list = i
            break
    if value in my_list:
        return True
    else:
        return False


if __name__ == '__main__':
    print('start')
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    a = search_value(data, 11)
    print(a)
