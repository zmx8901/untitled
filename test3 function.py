# # 定义函数
# def quadratic(a, b, c):
#     import math
#     d = math.sqrt(b * b - 4 * a * c)
#     x1 = (-b + d) / (2 * a)
#     x2 = (-b - d) / (2 * a)
#     return x1, x2
#
#
# print("quadratic(2, 3, 1)=", quadratic(2, 3, 1))
# for l in quadratic(2, 3, 1):
#     print(l)
#
#
# def powern(a, b=2):
#     return a ** b
#
#
# print(powern(2, 1))
# print(powern(5))
#
def calc(*numbers):  # 定义可变参数
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
num = (1, 2)
print(calc(*num))  # *nums表示把nums这个list的所有元素作为可变参数传进去


# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


args = [1, 2, 3, 4]
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)


# def iskong(s):
#     if 0 == len(s):
#         return s
# 将下列代码中重复代码替换会报错

def trim(s):
    if 0 == len(s):
        return s

    while ' ' == s[0]:
        s = s[1:]
        if 0 == len(s):
            return s

    while ' ' == s[-1]:
        s = s[:-1]
        if 0 == len(s):
            return s
    return s


print(trim(" "))



