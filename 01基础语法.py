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
# s3 = """
#     Hello:
#     欢迎大家进入到Python课程的学习!
#     大家记得一键三连哦 ~
#     """
# print(s3)
# print(type(s3))#<class 'str'>

# 转义字符 \' \"  \n  \t
# msg = 'It\'s very good'
# print(msg)
# msg2 = "It's very good"
# print(msg2)
# msg3 = "Hello 的意思就是 \"您好\""
# print(msg3)
# msg4 = 'Hello 的意思就是 \"您好\"'
# print(msg4)
# print("\t欢迎大家进入到Python课程的学习!\n\t大家记得一键三连哦 ~")  # \n 换行   \t  按了Tab缩进

# 字符串格式化
# 方式一:  %s 占位符
# name = "涛哥"
# age = 18
# pro = "软件工程"
# hobby = "Python、Java"
# print("大家好, 我是 %s , 今年 %s 岁, 学习的专业是 %s , 爱好 %s" % (name, age, pro, hobby))

#方式二:  f".. {变量名/表达式} .."  -----> 推荐方式
# name = "涛哥"
# age = 18
# pro = "软件工程"
# hobby = "Python、Java"
# print(f"大家好, 我是 {name} , 今年 {age} 岁, 学习的专业是 {pro} , 爱好 {hobby}")

# 输入输出语法
# a=input()
# print(a)
# password = input("请输入您的银行卡密码: ")#先输出后输入
# print(f"密码正确, {password}")#直接输出

#运算符
# print("10 // 4 = ", 10 // 4) # 整除(结果为整数) - 2
# print("10 % 4 = ", 10 % 4)  # 取余/求模 - 2
# print("10 ** 4 = ", 10 ** 4) # 幂指数, 10的4次方 - 10000

# 数据类型转换
# b=10.3
# print(int(b))
# print(b)#使用int()之后不修改原值
# print(float(b))

# 赋值运算符: = += -= *= /= %= //= **=

# 比较运算符: ==  !=  >  >=  <  <=

# 逻辑运算符: and   or   not

# 条件语句：（缩进很重要）（条件不使用括号包裹）
# if 条件:
#     执行语句
# elif 条件:
#     执行语句
# else:
#     执行语句

# match...case 模式匹配
# num1 = float(input("请输入第一个数: "))
# num2 = float(input("请输入第二个数: "))
# oper = input("请输入运算符(+ - * /) : ")
# match oper:
#     case "+":
#         print(f"{num1} + {num2} = {num1 + num2}")
#     case "-":
#         print(f"{num1} - {num2} = {num1 - num2}")
#     case "*":
#         print(f"{num1} * {num2} = {num1 * num2}")
#     case "/" if num2 != 0: # if条件成立, 才匹配这个case
#         print(f"{num1} / {num2} = {num1 / num2}")
#     case _:
#         print("操作不支持!!!")

# while循环
# i = 0
# while i < 10:
#     print("人生苦短, 我用Python~")
#     i += 1
# else:
#     print("循环结束")
# # 注意以上代码不等同于以下代码：
# i = 0
# while i < 10:
#     print("人生苦短, 我用Python~")
#     i += 1
# print("循环结束")
# 区别在于：
# 没有 break 时：两者确实等价
# 有 break 时：
# while...else 的 print("循环结束") 在被 break 之后不会被执行
# 但是没有 else 的语句中，即使有 break，print("循环结束")也会被执行到
# 总结来说呢，第一个示例中，print("循环结束")是不独立于while这个循环的，但第二个示例中print("循环结束")是独立的，不受while执行情况的影响

# for循环字符串
# msg = input("请输入需要遍历的字符串: ")
# for s in msg: # s 表示遍历出来的元素 ;  msg 表示需要遍历的数据
#     print(f"元素: {s}")

# for循环整数
# total=0
# for i in range(1, 101):
#     if i % 2 == 1: # 奇数
#         total += i
# 以上等同于：
# for i in range(1, 101, 2):
#     total += i
# 又等同于：
# for i in range(100)[1::2]:  # 1到99，步长2
#     total += i
# 这里的第三个变量是步长，也就是从1开始遍历到101，每次增长2，也就是1 3 5 7等等
# for循环中依然可能有else语句，执行与否也是受是否有break而决定

# x, y, z = "Orange", "Banana", "Cherry"
# x = y = z = "Orange"

# 以下内容报错
# x = 10
# y = "Bill"
# print(x + y)

# 全局变量VS局部变量：在函数外部or内部定义的变量，全局均可以使用，局部仅函数内部可以使用
# global关键字
# def myfunc():
#   global x
#   x = "fantastic"
# myfunc()
# print("Python is " + x)# Python is fantastic