class Fibonacci:
    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[0] = 0
            elif n == 1:
                self.cache[1] = 1
            else:
                self.cache[n] = self(n - 1) + self(n - 2)

        return self.cache[n]


fib = Fibonacci()
for i in range(8):
    print(fib(i))

print(fib.cache)


def fib(n):
    res = []
    for i in range(n):
        if i == 0:
            res.append(0)
        elif i == 1:
            res.append(1)
        else:
            res.append(res[-1] + res[-2])

    return res


print(fib(8))


