print('Введите колличество повторений: ')
n = int(input())
res = 0
def fac(k):
    if k == 0:
        return 1
    return fac(k-1) * k
def func_1(res, k):
    while k < n:
        res += (-1)*k*((5-k)/(fac(k)))
        k += 1
    return(res)

print('Сумма = ', round(func_1(0, 1), 2))
