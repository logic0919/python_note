# 日期时间
'''
import datetime
x = datetime.datetime.now()
print(x)
'''

# 数学
'''
import math
'''

# json
'''
import json

x='{ "name":"Bill", "age":63, "city":"Seatle"}'
json.loads(x)

y={
  "name": "Bill",
  "age": 63,
  "city": "Seatle"
}
json.dumps(y)
'''

# 正则
# 1.四个函数：
# findall()：提取所有匹配项，返回列表
# search()：遍历整个字符串，只匹配第一个，返回Match对象
# match()：只从字符串最开头匹配，开头不满足直接匹配失败；
# split()：按匹配到的内容分割字符串
# sub()：批量替换匹配内容
# 2.match对象
# first_phone.group()：字符串
# first_phone.group(n)：匹配的第n个分组（这里所谓的分组概念也就是一个()中的一个匹配结果）
# first_phone.start()：在原始字符串中的起始下标
# first_phone.end()：在原始字符串中的结束下标
# first_phone.span()：同时返回起止下标，格式 (start, end)
# first_phone.string：原始字符串（注意和group()不一样，group()表示的是被匹配到的那部分字符串，而string表示的是原本的完整的字符串）
# 3.列表推导式
# [i for i in addr_list if i]：
# 表示遍历addr_list也就是for i in addr_list，然后将其中的每一项i进行判空也就是if i，如果不为空则放入列表中也就是最开始的i
# 4.r表示不被转义
# r'(1\d{3})\d{4}(\d{3})'：()一个括号中的叫一个分组
# r'\1****\2'：这里的r表示引号中的\不被转义，也就是直接就是\1和\2，\1表示第一个分组也就是(1\d{3})也就是前四位，类似的，\2表示第二个分组也就是(\d{3})也就是最后三位
'''
import re

# 原始多行测试文本：包含手机号、数字、多余符号、混杂内容
content = """
订单编号：A001-9876
客户：张三 电话：13812345678
备用号码 13988887777
消费金额：199、299、399
备注###无用符号####2025年活动
地址：北京市朝阳区，海淀区；东城区  西城区
"""

# 正则规则
phone_rule = r'1[3-9]\d{9}'   # 匹配11位手机号
num_rule = r'\d+'             # 匹配所有纯数字
symbol_rule = r'#+'           # 匹配连续#符号
split_rule = r'[，； ]'        # 中文逗号、分号、空格作为分隔符

# 1. re.findall() 提取所有匹配项，返回列表
all_phone = re.findall(phone_rule, content)
all_num = re.findall(num_rule, content)
print("1.findall 提取全部手机号：", all_phone)
print("1.findall 提取全部数字：", all_num)
print("-" * 60)

# 2. re.search() 只匹配第一个，返回Match对象
first_phone = re.search(phone_rule, content)
if first_phone:
    print("2.search 第一个匹配手机号：", first_phone.group())
    print("匹配起始下标：", first_phone.start())
    print("匹配结束下标：", first_phone.end())
else:
    print("未匹配到内容")
print("-" * 60)

# 3. re.split() 按匹配到的内容分割字符串
addr_text = "北京市朝阳区，海淀区；东城区  西城区"
addr_list = re.split(split_rule, addr_text)
# 过滤分割后空字符串
addr_list = [i for i in addr_list if i]
print("3.split 分割地址：", addr_list)
print("-" * 60)

# 4. re.sub() 批量替换匹配内容
# 场景1：把###全部替换为空（删除无用符号）
clean_text = re.sub(symbol_rule, "", content)
print("4.sub 删除#符号后的文本：\n", clean_text)

# 场景2：手机号脱敏，中间4位替换为****
hide_phone_rule = r'(1\d{3})\d{4}(\d{3})'
hide_text = re.sub(hide_phone_rule, r'\1****\2', content)
print("\n4.sub 手机号脱敏文本：\n", hide_text)
'''
