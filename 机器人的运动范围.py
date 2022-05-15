class Solution:

    def get_counts(self, k, key: list, all: list):
        new = []
        for m in key:
            a = m[0]
            b = m[1]
            for i, j in ((a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1)):
                if i >= 0 and j >= 0:
                    num1 = self.get_sum(i)
                    num2 = self.get_sum(j)
                    print(num1, num2)
                    if num1 + num2 <= k:
                        if (i, j) not in key and (i, j) not in all:
                            new.append((i, j))
                            all.append((i, j))
        if new:
            new, all = self.get_counts(k, new, all)
        return new, all

    def get_sum(self, num):
        sum = 0
        for i in range(100):
            v = 10
            jude = num % v
            if jude == 0:
                pass
            else:
                sum += jude
            num = int(num / v)
        return sum


if __name__ == '__main__':
    print('start')
    a = Solution()
    b, c = a.get_counts(2, [[0, 0]], [])
    print(c)
    # c = a.get_sum(105)
    # print(c)
