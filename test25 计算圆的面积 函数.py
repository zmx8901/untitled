#计算圆的面积
'''
定义圆和面积计算函数
调用面积函数计算面积
'''
def rarea(r):
    PI = 3.14
    return PI*r**2
# print('圆的面积为：{:0.2f}'.format(rarea(5)))
print('圆的面积为：%0.2f'%rarea(5))