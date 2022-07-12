class GetList:

    def main(self, data: list):
        key_list = []
        mid_dic = {}
        for item in data:
            if item not in key_list:
                key_list.append(item)
                mid_dic[item] = 1
            else:
                mid_dic[item] += 1
        value_list = []
        for key in mid_dic:
            value_list.append(mid_dic[key])
        result_list = []
        for i in range(len(key_list)):
            index = value_list.index(max(value_list))
            result_list.append(key_list[index])
            key_list.remove(key_list[index])
            value_list.remove(max(value_list))
        return result_list


if __name__ == '__main__':
    obj = GetList()
    res = obj.main([1, 1, 4, 3, 9, 11, 3, 4, 3, 5, 1])
    print(res)
