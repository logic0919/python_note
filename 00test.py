import numpy as np

# 一、特点：
# 1.可以放一维、二维、三维甚至更高维数据
# 2.内部数据类型要求一致

# 二、创建
# （一）一般创建
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# （二）特殊创建之函数本身确定填充值而参数规定形状
# 1.零矩阵、全1矩阵、单位矩阵
c = np.zeros((3, 3))
d = np.ones((3, 3))
e = np.eye(3)  # 三阶单位矩阵

# 2.均匀分布（0~1之间）
f = np.random.rand(3, 3)                # [0,1)均匀分布，形状直接写参数
g = np.random.random((3, 3))            # [0,1)均匀分布，形状必须传元组
# 3.均匀分布（非0~1，自行指定范围）
h = np.random.uniform(5, 10, (3, 3))    # [5,10) 区间的均匀分布小数，形状传元组

# 4.标准正态分布（均值0，方差1）
i = np.random.randn(3, 3)               # 标准正态分布，形状直接写参数
# 5.正态分布（自己制定均值和方差）
j = np.random.normal(0, 1, (3, 3))      # 正态分布（可自定义均值和标准差），形状传元组

# 6.随机整数（指定范围）
k = np.random.randint(0, 10, (3, 3))    # [0,10) 区间的随机整数，形状传元组
l = np.random.choice(10, (3, 3))        # 从 0~9 中随机抽取整数，可放回抽样
m = np.random.choice([1, 3, 5, 7, 9], (3, 3))  # 从指定列表中随机抽取

# 三、特殊创建之函数本身确定形状而参数规定填充内容
# 1.类似于切片，一维等差数列
n = np.arange(5)           # 一个参数：从0开始，步长1，不包含5 → [0, 1, 2, 3, 4]
o = np.arange(1, 6)        # 两个参数：起始1，结束6（不包含），步长默认1 → [1, 2, 3, 4, 5]
p = np.arange(1, 10, 2)    # 一维，等差数列，[1,10)，步长为2
# 2.给定范围和总长度，均匀取值，一维
q = np.linspace(1, 10, 3) # [1,10]均匀取3个点，左闭右闭
r = np.linspace(0, 10, 5, endpoint=False)  # 不包含终点10

# 四、数组核心属性
print("===== 数组属性 =====")
print("shape形状：", b.shape)
print("ndim维度数：", b.ndim)
print("size总元素数：", b.size)
print("dtype数据类型：", b.dtype)
print("itemsize单个元素字节：", b.itemsize)
print("T转置：\n", b.T)

# 五、维度形状变换
print("\n===== 形状变换 =====")
b1 = b.reshape(1, 9)   # 重塑为1行9列
b2 = b.reshape(9,)     # 重塑为一维
b3 = b.flatten()       # 展平一维（拷贝）
b4 = b.ravel()         # 展平一维（优先视图）
b_copy = b.copy()
b_copy.resize(2, 5)    # 原地修改形状，不足补0
print("reshape(1,9)：", b1)
print("flatten展平：", b3)
print("resize原地修改：\n", b_copy)

# 六、索引与切片
print("\n===== 索引切片 =====")
print("一维切片n[1:4]：", n[1:4])
print("二维单元素b[0,1]：", b[0, 1])
print("多行多列切片b[0:2,1:]：\n", b[0:2, 1:])
mask = b > 4
print("布尔索引b[b>4]：", b[mask])
print("花式索引[[0,2],[1,2]]：", b[[0, 2], [1, 2]])

# 七、数组拼接与分割
print("\n===== 拼接分割 =====")
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr_v = np.vstack((arr1, arr2))  # 垂直拼接（行增加）
arr_h = np.hstack((arr1, arr2))  # 水平拼接（列增加）
split_row = np.split(arr_v, 2, axis=0)  # 按行分割
split_col = np.split(arr_h, 2, axis=1)  # 按列分割
print("垂直拼接vstack：\n", arr_v)
print("水平拼接hstack：\n", arr_h)

# 八、数值运算（逐元素）
print("\n===== 基础四则运算 =====")
add_arr = b + 2
sub_arr = b - 1
mul_arr = b * 3
div_arr = b / 2
pow_arr = b ** 2
sqrt_arr = np.sqrt(b)
mod_arr = b % 2
print("数组+2：\n", add_arr)
print("数组平方：\n", pow_arr)
print("开平方：\n", sqrt_arr)

# 矩阵乘法
mat_mul1 = b @ b.T
mat_mul2 = np.dot(b, b.T)
print("\n矩阵乘法@：\n", mat_mul1)

# 九、统计函数
print("\n===== 统计函数 =====")
print("全部求和sum：", np.sum(b))
print("按列求和sum(axis=0)：", np.sum(b, axis=0))
print("按行求和sum(axis=1)：", np.sum(b, axis=1))
print("最大值max：", np.max(b))
print("最小值min：", np.min(b))
print("均值mean：", np.mean(b))
print("中位数median：", np.median(b))
print("标准差std：", np.std(b))
print("方差var：", np.var(b))
print("最大值展平下标argmax：", np.argmax(b))
print("最小值展平下标argmin：", np.argmin(b))

# 十、通用数组操作
print("\n===== 通用操作函数 =====")
b_deep = b.copy()  # 深拷贝
float_arr = b.astype(np.float32)  # 转换数据类型
clip_arr = b.clip(2, 7)  # 限制数值2~7
uniq_arr = np.unique(b)  # 数组去重
sort_arr = np.sort(b, axis=1)  # 每行排序
where_arr = np.where(b > 5, 10, 0)  # 条件替换
print("转float32：", float_arr.dtype)
print("clip限制2~7：\n", clip_arr)
print("unique去重：", uniq_arr)
print("where条件替换>5为10：\n", where_arr)

# 十一、维度扩充、压缩、复制
print("\n===== 轴维度操作 =====")
expand = np.expand_dims(a, axis=0)  # 新增维度
squeeze_arr = np.squeeze(expand)     # 删除长度为1的维度
tile_arr = np.tile(a, (2, 3))        # 整体平铺复制
repeat_arr = np.repeat(a, 2)         # 每个元素重复2次
print("expand_dims增维shape：", expand.shape)
print("tile平铺复制：\n", tile_arr)
print("repeat元素复制：", repeat_arr)

# 十二、线性代数工具
print("\n===== 线性代数 =====")
det_e = np.linalg.det(e)      # 行列式
inv_e = np.linalg.inv(e)      # 逆矩阵
eig_val, eig_vec = np.linalg.eig(b)  # 特征值、特征向量
print("单位矩阵行列式det：", det_e)
print("单位矩阵逆inv：\n", inv_e)
print("特征值eig_val：", eig_val)
