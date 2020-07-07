# 用filter求素数
# 用Python来实现这个算法，可以先构造一个从3开始的奇数序列：注意这是一个生成器，并且是一个无限序列。
def _odd_iter():  # 先构造一个从3开始的奇数序列
    n = 1
    while True:
        n = n + 2
        yield n  # 这是一个生成器，并且是一个无限序列。


# 定义一个筛选函数,筛选新的素数：
def _not_divisible(n):
    return lambda x: x % n > 0


# 定义一个生成器，不断返回下一个素数：这段不是很懂
def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# for n in primes():
#     if n < 10:
#         print(n)
#     else:
#         break


# 下面这段输出是正常的
L = primes()
for m in range(10):
    print(next(L))

# #下面为测试语句
# L = (next(primes()) for m in range(1, 10))
# print(next(L))
# print(next(L))  # 两个输出都是2，有问题

# print(next(primes()) for m in range(10))  # 这个语句输出为地址
# print([next(primes()) for m in range(10)])  # 这个语句输出全部为2
print(primes())  # 这个语句输出为地址，为惰性计算，如何输出 ，用了list()函数也不行
