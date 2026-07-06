'''
文本类型：	str
数值类型：	int, float, complex
序列类型：	list, tuple, range
映射类型：	dict
集合类型：	set, frozenset
布尔类型：	bool
二进制类型：	bytes, bytearray, memoryview

Python 编程语言中有四种集合数据类型：
列表（List）是一种有序和可更改的集合。允许重复的成员。
元组（Tuple）是一种有序且不可更改的集合。允许重复的成员。
集合（Set）是一个无序和无索引的集合。没有重复的成员。
词典（Dictionary）是一个无序，可变和有索引的集合。没有重复的成员。

！！！！！！序列包含：列表 元组 集合 词典 字符串

x = "Hello World"	str	
x = 29	int	
x = 29.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "Bill", "age" : 63}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview

如果希望指定数据类型，则您可以使用以下构造函数：
x = str("Hello World")	str	
x = int(29)	int	
x = float(29.5)	float	
x = complex(1j)	complex	
x = list(("apple", "banana", "cherry"))	list	
x = tuple(("apple", "banana", "cherry"))	tuple	
x = range(6)	range	
x = dict(name="Bill", age=36)	dict	
x = set(("apple", "banana", "cherry"))	set	
x = frozenset(("apple", "banana", "cherry"))	frozenset	
x = bool(5)	bool	
x = bytes(5)	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
'''

# 1.数值类型
# 类型转换：您可以使用 int()、float() 和 complex() 方法从一种类型转换为另一种类型：
# 复数
# x = 2+3j
# y = 7j
# z = -7j

# 2.字符串
'''
注意：所有字符串方法都返回新值。它们不会更改原始字符串。

capitalize()	        把首字符转换为大写。
casefold()	            把字符串转换为小写。
center()	            返回居中的字符串。
count()	                返回指定值在字符串中出现的次数。
encode()	            返回字符串的编码版本。
endswith()	            如果字符串以指定值结尾，则返回 true。
expandtabs()	        设置字符串的 tab 尺寸。
find()	                在字符串中搜索指定的值并返回它被找到的位置。
format()	            格式化字符串中的指定值。
format_map()	        格式化字符串中的指定值。
index()	                在字符串中搜索指定的值并返回它被找到的位置。
isalnum()	            如果字符串中的所有字符都是字母数字，则返回 True。
isalpha()	            如果字符串中的所有字符都在字母表中，则返回 True。
isdecimal()	            如果字符串中的所有字符都是小数，则返回 True。
isdigit()	            如果字符串中的所有字符都是数字，则返回 True。
isidentifier()	        如果字符串是标识符，则返回 True。
islower()	            如果字符串中的所有字符都是小写，则返回 True。
isnumeric()	            如果字符串中的所有字符都是数，则返回 True。
isprintable()	        如果字符串中的所有字符都是可打印的，则返回 True。
isspace()	            如果字符串中的所有字符都是空白字符，则返回 True。
istitle()	            如果字符串遵循标题规则，则返回 True。
isupper()	            如果字符串中的所有字符都是大写，则返回 True。
join()	                把可迭代对象的元素连接到字符串的末尾。
ljust()	                返回字符串的左对齐版本。
lower()	                把字符串转换为小写。
lstrip()	            返回字符串的左修剪版本。
maketrans()	            返回在转换中使用的转换表。
partition()	            返回元组，其中的字符串被分为三部分。
replace()	            返回字符串，其中指定的值被替换为指定的值。
rfind()	                在字符串中搜索指定的值，并返回它被找到的最后位置。
rindex()	            在字符串中搜索指定的值，并返回它被找到的最后位置。
rjust()	                返回字符串的右对齐版本。
rpartition()	        返回元组，其中字符串分为三部分。
rsplit()	            在指定的分隔符处拆分字符串，并返回列表。
rstrip()	            返回字符串的右边修剪版本。
split()	                在指定的分隔符处拆分字符串，并返回列表。
splitlines()	        在换行符处拆分字符串并返回列表。
startswith()	        如果以指定值开头的字符串，则返回 true。
strip()	                返回字符串的剪裁版本。
swapcase()	            切换大小写，小写成为大写，反之亦然。
title()	                把每个单词的首字符转换为大写。
translate()	            返回被转换的字符串。
upper()	                把字符串转换为大写。
zfill()	                在字符串的开头填充指定数量的 0 值。
'''
# a = "Hello, World!"
# print(a[1])# 字符串是数组
# print(a[2:5])# llo
# print(a[-5:-2])# orl
# print(len(a))
# print(a.strip())# strip() 方法删除开头和结尾的空白字符
# print(a.lower())
# print(a.replace("World", "Kitty"))# replace() 用另一段字符串来替换字符串

# 3.布尔类型
'''
如果有某种内容，则几乎所有值都将评估为 True。
除空字符串外，任何字符串均为 True。
除 0 外，任何数字均为 True。
除空列表外，任何列表、元组、集合和字典均为 True。
'''

# 4.序列：字符串 列表 元组 集合 词典
'''
索引（正索引&负索引）

切片：[start（左闭）:end（右开）:step（步长）]
只有第二个冒号可以省略，也就是说最省的情况是[:]，表示整个序列

相加+
拼接两个相同数据类型的序列，但不会去重

相乘*
重复

in

not in

相关函数：
len()	        计算序列的长度，即返回序列中包含多少个元素。
max()	        找出序列中的最大元素。注意，对序列使用 sum() 函数时，做加和操作的必须都是数字，不能是字符或字符串，否则该函数将抛出异常，因为解释器无法判定是要做连接操作（+ 运算符可以连接两个序列），还是做加和操作。
min()	        找出序列中的最小元素。
list()	        将序列转换为列表。
str()	        将序列转换为字符串。
sum()	        计算元素和。
sorted()	    对元素进行排序。
reversed()	    反向序列中的元素。
enumerate()	    将序列组合为一个索引序列，多用在 for 循环中。
！！！！！！部分序列不能应用其中的部分函数，比如字典中不能直接使用list，详细的函数介绍请参阅相应数据类型的函数介绍。

'''

# 5.列表
# 列表（List）是一种有序和可更改的集合。允许重复的成员
# 内部可以是多种数据类型混合放，也可以列表里面套列表、元组等
'''
thislist = ["apple", "banana", "cherry"]

遍历：
for x in thislist:
  print(x)
  
append()：添加到末尾，可以添加一个元素，也可以是添加另一个列表
thislist.append("orange")
print(thislist)# ['apple', 'banana', 'cherry', 'orange']

insert()：添加到指定位置
thislist.insert(1, "orange")

remove()：删除指定元素
thislist.remove("orange")

pop()：删除指定位置，默认最后一个元素
x=thislist.pop(0)#x就是thislist[0]，thislist被修改了

del()：
del thislist[0]

clear()：
thislist.clear()# 变成空列表也就是[]

copy()：
x = fruits.copy()# x和fruits一样

count()：
x = fruits.count("cherry")# 计算fruits中有几个cherry

extend()：将指定的列表元素（或任何可迭代的元素）添加到当前列表的末尾。
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)

列表没有find()
字符串中有find()：找不到的话返回-1

index()：返回指定值首次出现的位置，找不到直接抛 ValueError 异常
x = fruits.index("cherry")

reverse()：方法反转元素的排序顺序。

sort()：默认情况下，sort() 方法对列表进行升序排序。
cars = ['Porsche', 'BMW', 'Volvo']
cars.sort()# 默认升序
cars.sort(reverse=True)# 指定逆序

list()：（其他，比如元组）转为列表
列表=list(元组)

tuple()：（其他，比如列表）转为元组
'''

# 6.元组
# 元组（Tuple）是一种有序且不可更改的集合。允许重复的成员。
# 无法 增 删 改
# # 内部可以是多种数据类型混合放，也可以元组里面套列表、元组等
'''
thistuple = ("apple", "banana", "cherry")

访问：print(thistuple[1])

索引

更改元组值：
创建元组后，您将无法更改其值。元组是不可变的，或者也称为恒定的。
但是有一种解决方法。您可以将元组转换为列表，更改列表，然后将列表转换回元组。
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

遍历：
for x in thistuple:
  print(x)
  
in，not in，len()

元组一旦创建，您就无法向其添加项目。元组是不可改变的。

创建单项元组：
thistuple = ("apple",)# 逗号很重要
而非：
thistuple = ("apple")# 字符串

无法删除某项元素，但是可以删除整个元组：
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) # 这会引发错误，因为元组已不存在

合并两个元组：+

tuple()：
语法：tuple(iterable)
参数必须是一个可迭代对象：字符串、列表、元组、集合等。
只能接收 0 个 或 1 个参数：0个就表示创建一个空元组
# 空元组
print(tuple())                                          # ()
# 传字符串（逐个拆字符）
print(tuple("hi"))                                      # ('h','i')
# 传列表
print(tuple([1,2,3]))                                   # (1,2,3)
# 传元组
thistuple = tuple(("apple", "banana", "cherry", 1))     # ('apple', 'banana', 'cherry', 1)

count()：

index()：
'''

# 7.列表、元组、集合的构造函数
# list ()、tuple ()、set () 构造函数规则完全一致：
# 只能传 0 个 或 1 个参数；
# 唯一参数必须是可迭代对象（字符串、列表、元组、range、集合等）；
# 不能直接写多个逗号隔开的值当参数，会报错。
# 小区别补充：
# list/tuple：允许存放可变元素（列表、集合、字典都能塞进去）；
# set：内部元素必须是可哈希，不能放列表、字典、集合这类可变对象。

# 8.集合
# 集合（Set）是一个无序和无索引的集合。没有重复的成员。
# 集合一旦创建，就无法更改项目，但是可以添加新项目，可以删除项目
'''
可以用for循环、in、not in、len()
不可以用索引

构造函数set()：
s = set()
print(s)  # set()
# 注意：{} 是空字典，不是空集合
print(set([1,2,2,3]))    # {1,2,3}
print(set((5,5,6)))      # {5,6}
print(set("aabbcc"))     # {'a','b','c'}
print(set(range(1,4)))   # {1,2,3}
s = set(1,2,3)           # 报错！传了2个参数
set([[1,2]])             # 报错，列表可变不能进集合
s = {1,2,3}              # 集合字面量创建（不用 set () 函数）

# 两次对一个集合进行打印操作，打印出来的顺序不一定相同
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
# {'cherry', 'orange', 'banana', 'apple'}
# {'banana', 'cherry', 'orange', 'apple'}

运算：
a = set([1,2,3])
b = set([3,4,5])
print(a & b)  # 交集 {3}
print(a | b)  # 并集 {1,2,3,4,5}
print(a - b)  # 差集 {1,2}

添加：
add()：添加一个
update()：添加多个
thisset.add("orange")
thisset.update(["orange", "mango", "grapes"])

删除：
remove()：指定元素
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana") 
如果指定的项目不存在，则 remove() 方法将引发错误

discard()：指定元素
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana") 
此方法与 remove() 方法不同，因为如果指定的项目不存在，则 remove() 方法将引发错误，而 discard() 方法不会。

pop()：此方法将删除最后一项。请记住，set 是无序的，因此您不会知道被删除的是什么项目。该函数返回值是被删除的元素

clear()：
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)# set()

del：
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) # 这将引发一个错误，因为该集合已不存在

交集判断：
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)

issubset()	返回另一个集合是否包含此集合。
issuperset()	返回此集合是否包含另一个集合。

合并
'''