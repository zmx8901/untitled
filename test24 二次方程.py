# 求解一元二次方案
import cmath

a = float(input('输入a:'))
b = float(input('输入b:'))
c = float(input('输入c:'))
# 计算过程
d = b ** 2 - 4 * a * c
sol1 = -b / (2 * a) + d
sol2 = -b / (2 * a) - d
# 输出结果
print('方程结果为{0:0.2f}和{1:0.3f}'.format(sol1, sol2))
