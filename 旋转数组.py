# 使用二分查找法实现, 核心：如果中间值小于前一位的值，则该值是最小值；如果小于最后的值，则说明在前半段；反之在后半段

def find_min(data):
    if not data:
        return None
    n = len(data) - 1
    start = 0
    end = n
    while start < end:
        mid = int((end + start) / 2)
        # print(mid)
        print(start, end)
        if data[mid] < data[mid - 1]:
            return mid
        if data[mid] < data[end]:
            end = mid - 1
        else:
            start = mid + 1


if __name__ == '__main__':
    print('start')
    data = [7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 6]
    t = find_min(data)
    print(data[t])
