# 测试print语句
print('%s' % 3.1415926)
print('Hello, %s,%s,%0.2f' % ('world', 3.1415926, 3.1415926))
# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
print('Age: %s. Gender: %s' % (25, True))

classmates = ['Michael', 'Bob', 'Tracy']  # 这是一个list
classmates.append('henry')
print(classmates, classmates[:2], classmates[2], ',"len(classmates)="', len(classmates))
classmates.insert(1, 'alon')
print(classmates, classmates[:2], classmates[2], ',"len(classmates)="', len(classmates))
classmates.pop()
print(classmates)
classmates.pop(-2)
print(classmates)
classmates[-1] = 'lucky'
print(classmates)

kongmaomao = (1,)
print(kongmaomao)
# kongmaomao[1]=2 元组一旦初始化就不能修改,下一行为元组中的可变性，采用list为元素
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][2], L[0: 2])

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

print(dict(Runoob=1, Google=2, Taobao=3))  # dict(d)  创建一个字典。d 必须是一个 (key, value)元组序列

for x in range(1, 11):
    # print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))
    print('{0:3d}{1:4d}{2:5d}'.format(x, x * x, x * x * x))
  # 以上语句作为换行输出
print('常量 PI 的值近似为：%5.3f。' % 3.14159)
print(f"常量 PI 的值近似为：{3.14159:5.3f}。")
print("常量 PI 的值近似为：{:5.3f}。".format(3.14159))
