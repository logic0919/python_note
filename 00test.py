import pandas as pd
import matplotlib.pyplot as plt

# 1. 构造测试数据
df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六", "钱七"],
    "语文": [85, 92, 78, 90, 88],
    "数学": [95, 80, 72, 88, 91]
})

# 设置中文显示（避免中文乱码）
plt.rcParams["font.family"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 2. 柱状图 kind="bar"
# 以下函数用于创建一个宽 6 英寸、高 4 英寸的空白画布
plt.figure(figsize=(8, 4))
# 以下代码中：plt.gca()：拿到当前画布上正在使用的坐标轴对象
# 指定 ax=plt.gca() = 强制让 pandas 在我们刚才创建的 figure 里绘图，而不是新开窗口。
df.plot(x="姓名", y=["语文", "数学"], kind="bar", ax=plt.gca())
plt.title("各科成绩柱状图")
plt.show()

# 3. 折线图 kind="line"
plt.figure(figsize=(8, 4))
df.plot(x="姓名", y="语文", kind="line", marker="o", ax=plt.gca())
plt.title("语文成绩折线图")
plt.show()

# 4. 直方图 kind="hist"（看分数分布）
plt.figure(figsize=(6, 4))
# bins=5：把数据的数值范围平均分成 5 段区间，统计每个区间内有多少条数据。
df["数学"].plot(kind="hist", bins=5, ax=plt.gca())
plt.title("数学成绩分布直方图")
plt.show()

# 5. 饼图 kind="pie"
plt.figure(figsize=(6, 6))
# df.set_index("姓名")：把表格的行索引替换为「姓名」列，原本的 0/1/2 数字索引消失，每行用姓名做标识，返回新 DataFrame。
df.set_index("姓名")["语文"].plot(kind="pie", autopct="%.1f%%", ax=plt.gca())
plt.title("语文成绩占比饼图")
plt.ylabel("")
plt.show()

# 6. 散点图 kind="scatter"
plt.figure(figsize=(6, 4))
df.plot(x="语文", y="数学", kind="scatter", s=80, ax=plt.gca())
plt.title("语文vs数学成绩散点图")
plt.show()