# 二分查找也称折半查找（Binary Search），它是一种效率较高的查找方法。但是，折半查找要求线性表必须采用顺序存储结构，而且表中元素按关键字有序排列
# 时间复杂度 logn

def binary_search(data: list, start, end, value):
    # print('start')
    if start > end:
        return -1
    mid = int((end - start) / 2 + start)
    # print(mid)
    if value == data[mid]:
        return mid
    elif value > data[mid]:
        return binary_search(data, mid + 1, end, value)
    elif value < data[mid]:
        return binary_search(data, start, mid - 1, value)
    else:
        return -1


if __name__ == '__main__':
    a = [1, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 16]  # len=12
    num = len(a) - 1
    c = binary_search(a, 0, num, 16)
    print(c)
    print(f'key:{c} ,value:{a[c]}')
