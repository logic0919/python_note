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
    iloc：无论是否自定义，都只认 0 开头的位置数字

'''
print("3. 取值筛选")
# 单列（Series）
print("单列df['姓名']：\n", df["姓名"])
# 多列（子df）
print("多列df[['姓名','分数']]：\n", df[["姓名","分数"]])
# 行切片
print("切片前3行 df[:3]：\n", df[:3])
# 布尔条件筛选
print("分数>90：\n", df[df["分数"] > 90])
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
# 按分数降序
df_sort = df.sort_values(by="分数", ascending=False)
print("按分数降序：\n", df_sort)
# 按索引排序
df_idx_sort = df.sort_index()
# 去重
df_dup = pd.concat([df, df.iloc[[0]]], ignore_index=True)
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
print("计数 count：", df["姓名"].count())
print("唯一值 unique：", df["年龄"].unique())
print("值计数 value_counts：\n", df["年龄"].value_counts())
print("="*60)

# ===================== 十、表格转换常用 =====================
print("10. 格式转换")
print("转字典 to_dict：\n", df.to_dict("records"))
print("转列表 to_list：\n", df["姓名"].tolist())
print("转Series单列 df['分数'].squeeze()：\n", df["分数"].squeeze())
# df.to_csv("data.csv", index=False) 保存csv
# df.to_excel("data.xlsx", index=False) 保存excel
