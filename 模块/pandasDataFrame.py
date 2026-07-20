import pandas as pd
import numpy as np

# 1. 构造测试DataFrame
data = [
    [88, 18, True],
    [92, 19, True],
    [76, 20, False]
]
# 自定义 index、columns 后，标签体系彻底替换掉默认 0,1,2 标签，只有 iloc 不受影响
df1 = pd.DataFrame(
    data,
    index=["s01", "s02", "s03"],    # 自定义行标签
    columns=["分数", "年龄", "及格"] # 自定义列名
)

data = {
    "姓名": ["小明", "小红", "小刚", "小丽", np.nan],
    "年龄": [18, 19, 20, 18, 21],
    "分数": [88.5, 92.0, 76.0, 95.5, 82.0],
    "是否及格": [True, True, False, True, True]
}
df = pd.DataFrame(data)
print("====原始df====")
print(df)
print("="*60)

# ===================== 一、常用属性 =====================
print("1. 基础信息属性")
print("df.values 底层数组：\n", df.values)
print("df.index 行索引：", df.index)
print("df.columns 列名：", df.columns)
print("df.dtypes 每列数据类型：\n", df.dtypes)
print("df.shape 行数,列数：", df.shape)
print("df.size 总元素个数：", df.size)
print("df.ndim 维度：", df.ndim)
print("df.empty 是否为空表：", df.empty)
print("df.columns.name 列索引名：", df.columns.name)
print("="*60)

# ===================== 二、查看数据方法 =====================
print("2. 查看数据")
print("前3行 head(3)：\n", df.head(3))
print("后2行 tail(2)：\n", df.tail(2))
print("随机2行 sample(2)：\n", df.sample(2))
print("基础信息 info()：")
df.info()
print("数值列统计 describe()：\n", df.describe())
print("="*60)

# ===================== 三、查询筛选（查） =====================
'''
1.	df[]
	只能单独取列 或 单独取行，不能同时指定行 + 列，无法精准定位单个单元格；
        传入字符串 / 字符串列表：取 列
        传入切片、布尔条件：取 行
2.	loc和iloc可以取行、列、单元格
    df.loc[行, 列]、df.iloc[行, 列] 
    语法支持「行，列」双参数，既能只取行、只取列，也能同时指定行列拿到单个单元格 / 一块子表格；
    loc：当没有自定义时必须使用隐式数字标签，当自定义时必须使用自定义的
        行维度：标签、标签切片、布尔数组、标签列表
        列维度：列名字符串、列名列表
    iloc：无论是否自定义，都只认 0 开头的位置数字
        行维度：纯数字、数字切片、数字下标列表
        列维度：纯数字、数字切片、数字下标列表
3. df.列名
    df.分数 等价于 df["分数"]
    条件限制（必须全部满足才能用点写法）：
        列名不含空格、加减乘除、横杠、括号等特殊符号
        列名不能和 pandas 内置属性重名（如 index、columns、size、loc、iloc、map 等）
        列名不能以数字开头
'''

'''
df['单列']	                        Series
df.loc[单行索引]	                    Series
df[['单列']]                         DataFrame
df.loc[[单行索引]]                    DataFrame
df[['列1','列2']]                    DataFrame
示例代码：
import pandas as pd
df = pd.DataFrame({"姓名":["张三","李四"],"分数":[90,80]})
print(type(df["分数"]))
print(type(df[["分数"]]))
print(type(df.loc[0]))
print(type(df.loc[[0]]))
print(type(df.loc[[0,1]]))
'''

print("3. 取值筛选")
# 单列（Series）
print("单列df['姓名']：\n", df["姓名"]) # 标签取列
# 多列（子df）
print("多列df[['姓名','分数']]：\n", df[["姓名","分数"]]) # 提取多个列用方括号嵌套 [[]]
# 行切片
print("切片前3行 df[:3]：\n", df[:3]) # 切片取行
# 布尔条件筛选
print("分数>90：\n", df[df["分数"] > 90]) # 分数>90的整行
# loc 标签索引 行,列
print("loc单行：\n", df.loc[1])
print("loc指定行列：\n", df.loc[[0,2], ["姓名","年龄"]])
# iloc 数字下标
print("iloc下标取第0、3行，第1、2列：\n", df.iloc[[0,3], [1,2]])
print("="*60)
# df.loc [行条件，列名]
# df.iloc [行下标，列下标]

# ===================== 四、修改数据（改） =====================
print("4. 修改")
df2 = df.copy()
# 修改整列
df2["年龄"] = df2["年龄"] + 1
# 条件修改
df2.loc[df2["分数"] < 80, "是否及格"] = False
print("修改后df2：\n", df2)
print("="*60)


# ===================== 五、新增行列（增） =====================
print("5. 新增行列")
df3 = df.copy()
# 新增列
df3["等级"] = df3["分数"].map(lambda x: "A" if x>=90 else "B")
# 新增行 concat
new_row = pd.DataFrame([{"姓名":"小华","年龄":19,"分数":89,"是否及格":True}])
df3 = pd.concat([df3, new_row], ignore_index=True)
print("新增行列后：\n", df3)
print("="*60)

# ===================== 六、删除行列（删） =====================
print("6. 删除")
df4 = df.copy()
# drop删列 axis=1
df4_1 = df4.drop("是否及格", axis=1)
print("删除列：\n", df4_1)
# drop删行
df4_2 = df4.drop([0,2], axis=0)
print("删除行：\n", df4_2)
# 条件删除（保留不等于18岁）
df4_3 = df4[df4["年龄"] != 18]
print("条件删除行：\n", df4_3)
print("="*60)

# ===================== 七、缺失值处理 =====================
print("7. 空值处理")
print("判断空值 isnull()：\n", df.isnull())
print("非空 notnull()：\n", df.notnull())
df5 = df.copy()
print("删除空行 dropna()：\n", df5.dropna())
print("填充空值 fillna('未知')：\n", df5.fillna("未知"))
print("="*60)

# ===================== 八、排序、去重 =====================
print("8. 排序、去重")
# 按分数这一列降序
df_sort = df.sort_values(by="分数", ascending=False)
print("按分数降序：\n", df_sort)
# 按索引排序——按行索引 index / 列名 columns排序
# 按照行名排序
df_idx_sort = df.sort_index()
# 等价于以下一行
df_sort.sort_index(axis=0)
# 按照列名排序
df_sort.sort_index(axis=1)

# 去重
df_dup = pd.concat([df, df.iloc[[0]]], ignore_index=True)
# 不传参数（默认）：整行所有列的值全部一模一样，才算重复，只保留第一次出现的行，后面重复行删掉。
# df.drop_duplicates(subset=["姓名","分数"])：只看你指定的几列，这几列相同就判定重复，其他列不管
# keep="first"（默认）：保留第一次出现的重复行，删后面重复的
# keep="last"：保留最后一条，删前面重复的
# keep=False：所有重复行全部删除，一条不留
# 这个函数天生只管行，重复列要单独处理，示例：df = df.T.drop_duplicates().T
print("去重 drop_duplicates：\n", df_dup.drop_duplicates())
print("="*60)

# ===================== 九、统计聚合方法 =====================
print("9. 聚合统计")
print("分数总和 sum：", df["分数"].sum())
print("平均分 mean：", df["分数"].mean())
print("最大值 max：", df["分数"].max())
print("最小值 min：", df["分数"].min())
print("中位数 median：", df["分数"].median())
print("标准差 std：", df["分数"].std())
print("计数 count：", df["姓名"].count()) # 统计该列一共有多少个非空数据
print("唯一值 unique：", df["年龄"].unique())
print("值计数 value_counts：\n", df["年龄"].value_counts()) # 看每个内容各自出现多少次，做频次统计
print("="*60)

# ===================== 十、表格转换常用 =====================
print("10. 格式转换")
print("转字典 to_dict：\n", df.to_dict("records"))
print("转列表 to_list：\n", df["姓名"].tolist())
print("转Series单列 df['分数'].squeeze()：\n", df["分数"].squeeze()) # 一行/一列都可以调用这个函数转为series
# df.to_csv("data.csv", index=False) 保存csv
# df.to_excel("data.xlsx", index=False) 保存excel

# pandas绘图————plot()
'''
示例代码：
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
'''