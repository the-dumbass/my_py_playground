def exp_sum(num):

    cache = {1: 1}

    def sums(n):
        adder = 0
        for i in range(2, n):
            if n // i - 1:
                adder += n // i - 1

        if n not in cache:
            cache[n] = sums(n - 1) + adder + 1
        return cache[n]

    return sums(num)


print(exp_sum(10))
