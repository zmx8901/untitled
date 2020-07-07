print("hello aalon 您好");
print("张明星，您好")
str = 'Hello World!'

print(str)  # 输出完整字符串
print(str[0])  # 输出字符串中的第一个字符
print(str[2:5])  # 输出字符串中第三个至第六个之间的字符串
print(str[2:])  # 输出从第三个字符开始的字符串
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 输出连接的字符串

print('以下基本运算：')
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))  # 注意这里的除的结果为浮点数，否则会取整
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))  # %% 为运算符,%表示取模 - 返回除法的余数
print('%d ** %d = %d' % (a, b, a ** b))
print(3 in (1, 2, 3))

a1 = b1 = c1 = 1, 2, 3
d, e, f = 4, 5, 'henry'
print(a1, b1, c1, '\n', d, e, f)  # 注意\n的用法，
