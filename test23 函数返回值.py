import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)  # 返回值是一个tuple


# 测试必选参数、默认参数、可变参数、关键字参数和命名关键字参数，廖雪峰官网
# 关键字参数(**kw)允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)  # 有对应关系的参数才是关键字参数，才能传入**kw
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
print('以下测试f2')


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f2(1, 2, d=99, ext=None)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
