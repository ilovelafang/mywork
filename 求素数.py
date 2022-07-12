class PrimeNum:

    def main(self, num):
        if not isinstance(num, int):
            print("请输入整数")
            return None
        k = num // 2
        for i in range(2, k):
            res = num % i
            if res == 0:
                x = i
                y = int(num / i)
                if self.is_prime(x) and self.is_prime(y):
                    return x, y
        return -1, -1

    def is_prime(self, m):
        half = m // 2
        res = []
        for i in range(1, half + 1):
            r = m % i
            if r == 0:
                res.append(i)
        if len(res) == 1:
            return True
        else:
            return False


if __name__ == '__main__':
    obj = PrimeNum()
    k = obj.main(15)
    print(k)
