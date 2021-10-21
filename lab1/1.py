class fib:
    def __init__(self, a0, a1):
        self.a0 = a0
        self.a1 = a1
        pass
    def cal(n):
        pass
    @classmethod
    def getDefault(cls):
        return cls(0, 1)

class fib_norm(fib):
    def __init__(self, a0, a1):
        super(a0, a1)
    
    def cal(n):
        for i in range(2, n):
            t = a0
            a0 = a1
            a1 = t
        return a1

class fib_quick(fib):
    def __init__(self, a0, a1):
        super().__init__(a0, a1)
        self.base = [[1, 1], [1, 0]]

    def __matrix_plus(m1, m2):
        res = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                res[i][j] = m1[i][j] + m2[i][j]
        return res

    def __matrix_mul(self, m1, m2):
        res = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    res[i][j] += m1[i][k] * m2[k][j];
        return res

    def cal(self, n):
        res = [[1, 0], [0, 1]]
        while(n):
            if (n & 1) :
                res = self.__matrix_mul(res, self.base)
            self.base = self.__matrix_mul(self.base, self.base)
            n = n >> 1
        return res[1][0] * a1 + res[1][1] * a0

class fib_factory:
    def __init__(self):
        pass

    @staticmethod
    def getInstance(type, a0, a1):
        if type == 'normal':
            return fib_norm(a0, a1)
        elif type == 'quick':
            return fib_quick(a0, a1)
    
    def getInstance(type):
        if type == 'normal':
            return fib_norm.getDefault()
        elif type == 'quick':
            return fib_quick.getDefault()

if __name__ == '__main__':
    # print('请输入a0和a1:')
    a0 = 1
    a1 = 1
    fib_x = fib_factory.getInstance("quick", a0, a1)
    print(fib_x.cal(10))
    pass