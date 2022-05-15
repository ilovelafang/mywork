from typing import List


# 回溯法求值
class Solution:

    def __init__(self, data: List[List[str]], string: str):
        self.data = data
        self.string = string

    def get_first(self):
        for i in self.data:
            for j in i:
                if j == self.string[0]:
                    a = self.data.index(i)
                    b = i.index(j)
                    return a, b
        return None

    def matrix_path(self):
        a, b = self.get_first()
        print(a, b)
        print(self.string[1:])
        key = [(a, b)]
        for k in self.string[1:]:
            count = 0
            for i, j in ((a, b + 1), (a, b - 1), (a - 1, b), (a + 1, b)):
                if 0 <= a and 0 <= b:
                    if self.data[i][j] == k:
                        ele = (i, j)
                        if ele not in key:
                            key.append(ele)
                            count += 1
                            a = i
                            b = j
                            break
            if count == 0:
                return False
        print(key)
        return True


if __name__ == '__main__':
    print('start')
    data = [['a', 'b', 'c', 'd'],
            ['g', 'h', 'i', 'j'],
            ['k', 'l', 'm', 'n'],
            ['o', 'p', 'q', 'r'],
            ['g', 'u', 'v', 'w']]
    word = 'bhiml'
    x = Solution(data, word)
    res = x.matrix_path()
    print(res)
