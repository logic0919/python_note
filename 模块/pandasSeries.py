import pandasSeries as pd
import numpy as np

# 1. 创建Series 4种方式
# 方式1：列表创建
s1 = pd.Series([12, 34, 56, 78, 90], name="数值列")
# 方式2：自定义索引
s2 = pd.Series([2.1, 3.2, 4.3], index=["a", "b", "c"], name="小数")
# 方式3：字典创建，key=索引，value=值
dic = {"张三": 88, "李四": 92, "王五": 76}
s3 = pd.Series(dic)
# 方式4：numpy数组创建
arr = np.array([10, 20, 30])
s4 = pd.Series(arr)

print("=== 原始Series ===")
print(s1)
print("-"*40)

# 2. 核心属性
print("=== 常用属性 ===")
print("值数组：", s1.values)
print("索引：", s1.index)
print("名称：", s1.name)
print("数据类型：", s1.dtype)
print("元素个数：", s1.size)
print("形状：", s1.shape)
print("是否有空值：", s1.hasnans)
print("前2行：\n", s1.head(2))
print("后2行：\n", s1.tail(2))
print("-"*40)

# 3. 取值、切片、索引
print("=== 索引取值 ===")
print("下标取第0个：", s1[0])
print("索引标签取值：", s2["b"])
print("切片 1~3：\n", s1[1:4])
print("布尔筛选 >50：\n", s1[s1 > 50])
print("-"*40)

# 4. 数值统计方法
print("=== 统计方法 ===")
print("总和：", s1.sum())
print("均值：", s1.mean())
print("最大值：", s1.max())
print("最小值：", s1.min())
print("中位数：", s1.median())
print("方差：", s1.var())
print("标准差：", s1.std())
print("描述性统计：\n", s1.describe())
print("唯一值：", s1.unique())
print("值计数（频次）：\n", s1.value_counts())
print("-"*40)

# 5. 数据修改、缺失值处理
# 造带空值序列
s5 = pd.Series([1, np.nan, 5, np.nan, 9])
print("=== 缺失值处理 ===")
print("原序列：\n", s5)
print("判断空值：\n", s5.isna())
print("非空值：\n", s5.notna())
print("删除空值：\n", s5.dropna())
print("填充空值为0：\n", s5.fillna(0))
print("填充均值：\n", s5.fillna(s5.mean()))
print("-"*40)

# 6. 类型转换、排序
print("=== 排序 & 类型转换 ===")
s6 = pd.Series([5, 2, 9, 1])
print("升序排序：\n", s6.sort_values())
print("降序排序：\n", s6.sort_values(ascending=False))
print("按索引排序：\n", s2.sort_index())
# 类型转换
s_str = pd.Series(["1","2","3"])
print("转数值：\n", s_str.astype(int))
print("-"*40)

# 7. 映射、替换、运算
print("=== 映射与替换 ===")
s7 = pd.Series([10,20,30])
print("全体+5：\n", s7 + 5)
print("全体乘2：\n", s7 * 2)
# replace替换值
print("替换10→100：\n", s7.replace(10, 100))
# map映射
def double(x):
    return x * 10
print("map自定义函数：\n", s7.map(double))
print("-"*40)

# 8. 去重、重置索引、转DataFrame
print("=== 格式转换操作 ===")
dup_s = pd.Series([1,1,2,2,3])
print("去重：\n", dup_s.drop_duplicates())
print("重置索引：\n", s1.reset_index(drop=True))
# Series 转 DataFrame
df = s1.to_frame()
print("转DataFrame：\n", df)
# 转列表/字典
print("转list：", s1.tolist())
print("转dict：", s3.to_dict())
