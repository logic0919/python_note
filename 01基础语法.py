# True/Flase首字母要大写，才是关键字
# print(,)格式，用英文逗号隔开，打印结果不显示英文逗号

# pycharm中快捷键
# 修改代码字体大小：shift+alt+,/. 分别是放小字体和放大字体

# 数据类型
# num = -100
# print(type(num)) #<class 'int'>
# print(isinstance(num, int)) #True
# print(isinstance(num, float)) #False
# print(isinstance(num, bool)) #False

# 三引号定义 (多行字符串)（保留换行和缩进）
'''
s3 = """
    Hello:
    欢迎大家进入到Python课程的学习!
    大家记得一键三连哦 ~
    """
print(s3)
print(type(s3))#<class 'str'>
'''

# 转义字符 \' \"  \n  \t
'''
msg = 'It\'s very good'
print(msg)
msg2 = "It's very good"
print(msg2)
msg3 = "Hello 的意思就是 \"您好\""
print(msg3)
msg4 = 'Hello 的意思就是 \"您好\"'
print(msg4)
print("\t欢迎大家进入到Python课程的学习!\n\t大家记得一键三连哦 ~")  # \n 换行   \t  按了Tab缩进
'''

# 字符串格式化
'''
方式一:  %s 占位符
name = "涛哥"
age = 18
pro = "软件工程"
hobby = "Python、Java"
print("大家好, 我是 %s , 今年 %s 岁, 学习的专业是 %s , 爱好 %s" % (name, age, pro, hobby))

方式二:  f".. {变量名/表达式} .."  -----> 推荐方式（f-string）
name = "涛哥"
age = 18
pro = "软件工程"
hobby = "Python、Java"
print(f"大家好, 我是 {name} , 今年 {age} 岁, 学习的专业是 {pro} , 爱好 {hobby}")

方式三：str.format()
'''

# 输入输出语法
'''
a=input()
print(a)
password = input("请输入您的银行卡密码: ")#先输出后输入
print(f"密码正确, {password}")#直接输出
'''

#运算符
'''
print("10 // 4 = ", 10 // 4) # 整除(结果为整数) - 2
print("10 % 4 = ", 10 % 4)  # 取余/求模 - 2
print("10 ** 4 = ", 10 ** 4) # 幂指数, 10的4次方 - 10000
'''

# 数据类型转换
'''
b=10.3
print(int(b))
print(b)#使用int()之后不修改原值
print(float(b))
'''

# 赋值运算符: = += -= *= /= %= //= **=

# 比较运算符: ==  !=  >  >=  <  <=

# 逻辑运算符: and   or   not

# 条件语句：（缩进很重要）（条件不使用括号包裹）
'''
if 条件:
    执行语句
elif 条件:
    执行语句
else:
    执行语句
    '''

# match...case 模式匹配
'''
num1 = float(input("请输入第一个数: "))
num2 = float(input("请输入第二个数: "))
oper = input("请输入运算符(+ - * /) : ")
match oper:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/" if num2 != 0: # if条件成立, 才匹配这个case
        print(f"{num1} / {num2} = {num1 / num2}")
    case _:
        print("操作不支持!!!")
'''

# while循环
'''
i = 0
while i < 10:
    print("人生苦短, 我用Python~")
    i += 1
else:
    print("循环结束")
# 注意以上代码不等同于以下代码：
i = 0
while i < 10:
    print("人生苦短, 我用Python~")
    i += 1
print("循环结束")
区别在于：
没有 break 时：两者确实等价
有 break 时：
while...else 的 print("循环结束") 在被 break 之后不会被执行
但是没有 else 的语句中，即使有 break，print("循环结束")也会被执行到
总结来说呢，第一个示例中，print("循环结束")是不独立于while这个循环的，但第二个示例中print("循环结束")是独立的，不受while执行情况的影响
'''

# for循环
'''
for循环字符串
msg = input("请输入需要遍历的字符串: ")
for s in msg: # s 表示遍历出来的元素 ;  msg 表示需要遍历的数据
    print(f"元素: {s}")

for循环整数
total=0
for i in range(1, 101):
    if i % 2 == 1: # 奇数
        total += i
以上等同于：
for i in range(1, 101, 2):
    total += i
又等同于：
for i in range(100)[1::2]:  # 1到99，步长2
    total += i
这里的第三个变量是步长，也就是从1开始遍历到101，每次增长2，也就是1 3 5 7等等
for循环中依然可能有else语句，执行与否也是受是否有break而决定
'''

# x, y, z = "Orange", "Banana", "Cherry"
# x = y = z = "Orange"

# 以下内容报错
# x = 10
# y = "Bill"
# print(x + y)

# 全局变量VS局部变量：
'''
在函数外部or内部定义的变量，全局均可以使用，局部仅函数内部可以使用
global关键字
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)# Python is fantastic
'''

# 匿名函数lambda
# lambda 函数可接受任意数量的参数，但只能有一个表达式。
'''
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11)) # 22
print(mytripler(11)) # 33
'''

# 类和对象
'''
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)

class Person:
# 注意：每次使用类创建新对象时，都会自动调用 __init__() 函数。
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
p1 = Person("Bill", 63)
print(p1.name)
print(p1.age)
p1.myfunc()
p1.age = 10 # 修改属性
del p1.age # 删除属性
del p1 # 删除整个对象
'''

# 继承
'''
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
# 使用 Person 来创建对象，然后执行 printname 方法：
x = Person("Bill", "Gates")
x.printname()

# 子类继承
class Student(Person):
  pass # 注意：如果您不想向该类添加任何其他属性或方法，请使用 pass 关键字。

# 为 Student 类添加 __init__() 函数：
class Student(Person):
  def __init__(self, fname, lname):
    # 添加属性等
# 注意：子的 __init__() 函数会覆盖对父的 __init__() 函数的继承。

# 如需保持父的 __init__() 函数的继承，请添加对父的 __init__() 函数的调用：
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
    
# super() 函数、添加属性、添加方法
Python 还有一个 super() 函数，它会使子类从其父继承所有方法和属性：
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname) # 通过使用 super() 函数，您不必使用父元素的名称，它将自动从其父元素继承方法和属性。
    self.graduationyear = year # 给子类添加属性
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
# 提示：如果您在子类中添加一个与父类中的函数同名的方法，则将覆盖父方法的继承。
x = Student("Elon", "Musk", 2019)
'''

# 多态
# 函数多态：同一个函数对于不同角色执行不同操作。一个可用于不同对象的 Python 函数的例子是 len() 函数。
# 类多态：
# 继承类多态：
'''
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Move!")
    
class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") # 创建 Car 对象
boat1 = Boat("Ibiza", "Touring 20") # 创建 Boat 对象
plane1 = Plane("Boeing", "747") # 创建 Plane 对象

for x in (car1, boat1, plane1):
  x.move()
'''

# 模块
'''
dir函数：
该内置函数可以列出模块中的所有函数名（或变量名）
import platform
x = dir(platform)
print(x)

部分导入：
模块内容：
def greeting(name):
  print("Hello, " + name)
person1 = {
  "name": "Bill",
  "age": 63,
  "country": "USA"
}
导入：
from mymodule import person1
print (person1["age"])
'''

# 异常捕获
'''
1.流程：
try:
  print(x)
except NameError:
  print("Variable x is not defined") # 对指定类型的异常已经捕获
except:
  print("Something else went wrong") # 如果异常在前面的捕获指定类型阶段未能捕获到，就进入这里，这里对所有的都能捕获到
else:
  print("Nothing went wrong") # 如果没有异常就执行这里
finally:
  print("The 'try except' is finished") # 无论是否有异常都会执行

2.主动抛出异常raise
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")

x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")
'''

# is运算符
'''
is 运算符（和 == 完全不一样）：
==：判断两个值是否相等
is：判断两个是不是同一个对象（内存地址完全相同）

用途：
1. 类型判断：type(x) is int
2. None判断：只用 is None
3. 小整数池：-5 ~ 256 数字复用对象。这个区间的数字全局共用一块内存，所以 is 返回 True
4. 判断布尔值：可用 is True
5. 自定义类对象判断：
class Person:
    pass
p1 = Person()
p2 = Person()
p3 = p1
print(p1 is p2) # False
print(p1 is p3) # True
6. 字符串常量池，短字符串共用对象
s1 = "hello"
s2 = "hello"
print(s1 is s2) # True
s3 = "hello world"
s4 = "hello" + " world"
print(s3 is s4) # True
'''