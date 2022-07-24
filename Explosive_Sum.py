from itertools import product as pro, combinations_with_replacement as com


def exp_sum(num):
    ints = list(range(1, num))
    sums = 1
    for i in ints:
        for j in com(ints, i):
            if sum(j) == num:
                # print(j)
                sums += 1
    return sums + 1 if num > 1 else 1


print(exp_sum(6))