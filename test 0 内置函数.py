'''
all() 函数
用于判断给定的可迭代参数 iterable <元组或列表>中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
元素除了是 0、空、None、False 外都算 True。
all(iterable)
'''
print("---以下all()函数---")
A = all(['a', 'b', '', 'd'])  # 列表list和元组tuple，存在一个空元素或0
B = all([])  # 空列表和空元组
print(A)
print(B)
print(all([]) )
'''
any() 函数
用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
元素除了是 0、空、FALSE 外都算 TRUE。
any(iterable)
'''
print("---以下any()函数---")
print(any([0, '', False]) )
print(any([]) )
'''
basestring() 方法
是 str 和 unicode 的超类（父类），也是抽象类，因此不能被调用和实例化，但可以被用来判断一个对象是否为 str 或者 unicode 的实例，
isinstance(obj, basestring) 等价于 isinstance(obj, (str, unicode))。
basestring() 无参数
'''
#print(isinstance("Hello world", basestring))  name 'basestring' is not defined
'''
bin() 
返回一个整数 int 或者长整数 long int 的二进制表示。
bin(x)
'''
print("---以下bin ()函数---")
print(bin(10))
'''
callable() 函数用于检查一个对象是否是可调用的。如果返回 True，object 仍然可能调用失败；但如果返回 False，调用对象 object 绝对不会成功。
对于函数、方法、lambda 函式、 类以及实现了 __call__ 方法的类实例, 它都返回 True。
callable(object)
'''
'''
chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
chr(i)  i -- 可以是10进制也可以是16进制的形式的数字。
'''
print("---以下chr ()函数---")
print( chr(0x30), chr(0x31), chr(0x61))
'''
cmp(x,y) 函数
用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。
cmp( x, y )  x y -- 数值表达式。
Python 3.X 的版本中已经没有 cmp 函数，如果你需要实现比较功能，需要引入 operator 模块，适合任何对象
，包含的方法有：
import operator
operator.eq('hello', 'name');
operator.gt(a, b)
operator.__lt__(a, b)
'''
'''
compile() 函数将一个字符串编译为字节代码。
compile(source, filename, mode[, flags[, dont_inherit]])
'''

'''
dict() 函数
用于创建一个字典。
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
**kwargs -- 关键字
mapping -- 元素的容器。
iterable -- 可迭代对象。
'''
print("---以下dict()函数---")
print(dict(a='a', b='b', t='t')  )
'''
dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。
如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
dir([object])
object -- 对象、变量、类型。
dir()   #  获得当前模块的属性列表
dir([ ])    # 查看列表的方法
'''
'''
divmod() 函数
把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
在 python 2.3 版本之前不允许处理复数。
divmod(a, b)  a b 数字
'''
print("---以下divmod()函数---")
print(divmod(7, 2))
# print(divmod(1+2j,1+0.5j))
'''
enumerate() 函数
用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
Python 2.3. 以上版本可用，2.6 添加 start 参数。
enumerate(sequence, [start=0])
sequence -- 一个序列、迭代器或其他支持迭代对象。
start -- 下标起始位置。
'''
print("---以下enumerate()函数---")
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))

x = 7
eval( '3 * x' )
'''
filter() 函数
用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
filter(function, iterable)
function -- 判断函数。
iterable -- 可迭代对象。
'''
'''
Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。
基本语法是通过 {} 和 : 来代替以前的 % 。
format 函数可以接受不限个参数，位置可以不按顺序。
"{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序
"{0} {1}".format("hello", "world")  # 设置指定位置
"{1} {0} {1}".format("hello", "world")  # 设置指定位置
'world hello world'
'''
print("---以下format()函数---")
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))

# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的
'''
frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
class frozenset([iterable])
iterable -- 可迭代的对象，比如列表、字典、元组等等。
返回新的 frozenset 对象，如果不提供任何参数，默认会生成空集合。
'''
'''
globals() 函数会以字典类型返回当前位置的全部全局变量。
getattr() 函数用于返回一个对象属性值。
hasattr() 函数用于判断对象是否包含对应的属性。
setattr() 函数对应函数 getattr()，用于设置属性值，该属性不一定是存在的。
hex() 函数用于将一个指定数字转换为 16 进制数。
id() 函数用于获取对象的内存地址。
'''
'''
 input() 函数
 接受一个标准输入数据，返回为 string 类型。
 input([prompt])
'''
'''
isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
isinstance() 与 type() 区别：
type() 不会认为子类是一种父类类型，不考虑继承关系。
isinstance() 会认为子类是一种父类类型，考虑继承关系。
如果要判断两个类型是否相同推荐使用 isinstance()。
isinstance(object, classinfo)
object -- 实例对象。
classinfo -- 可以是直接或间接类名、基本类型或者由它们组成的元组。
'''
print("---以下isinstance()函数---")
print(isinstance (1,int),isinstance (2,(str,int,list)) )
'''
list() 方法用于将元组或字符串转换为列表。
注：元组与列表是非常类似的，区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中。
map() 会根据提供的函数对指定序列做映射。
map(function, iterable, ...)
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
'''
print("---以下map()函数---")
import math
# 以下用print输出有误
# map(x**2, [1,2,3,4,5])  # 计算列表各个元素的平方
# map(lambda x: x ** 2, [1, 2, 3, 4, 5]) # 使用 lambda 匿名函数