import numpy as np

# 一、特点：
# 1.可以放一维、二维、三维甚至更高维数据
# 2.内部数据类型要求一致
# 3.所有算数、大小比较、逻辑判断，全部作用在数组每一个独立元素上，底层 C 实现，速度远快于 Python for 循环。
#     比如 布尔判断 四则运算、加减乘除 两个数组之间运算（同形状） 广播机制（数组和不同维度数字 / 数组运算）

# 二、创建
# （一）一般创建
a=np.array([1,2,3])
b=np.array([[1,2,3],[4,5,6],[7,8,9]])

# （二）特殊创建之函数本身确定填充值而参数规定形状
# 1.
c=np.zeros((3,3))
d=np.ones((3,3))
e=np.eye(3) # 三阶单位矩阵

# 2.均匀分布（0~1之间）
f = np.random.rand(3, 3)                # [0,1)均匀分布，形状直接写参数
g = np.random.random((3, 3))            # [0,1)均匀分布，形状必须传元组
# 3.均匀分布（非0~1，自行指定范围）===
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
# 1.类似于切片，一维
# 也可以使用浮点数的步长，但不推荐
n = np.arange(5)           # 一个参数：从0开始，步长1，不包含5 → [0, 1, 2, 3, 4]
o = np.arange(1, 6)        # 两个参数：起始1，结束6（不包含），步长默认1 → [1, 2, 3, 4, 5]
p = np.arange(1, 10, 2) # 一维，等差数列，[1,10)，步长为2
# 2.给定范围和总长度，均匀取值，一维
q=np.linspace(1, 10, 3) # [1,10]的10各数据均匀分布，默认左闭右闭
r=np.linspace(0, 10, 5, endpoint=False)  # 不包含终点10

# 四、常用属性
a1 = np.array([[[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]],
               [[13, 14, 15, 16],
                [17, 18, 19, 20],
                [21, 22, 23, 24]]])
# 1. shape - 查看数组的形状（各维度大小）
print(f"a1.shape = {a1.shape}")           # (2, 3, 4) → 2层，3行，4列
# 2. ndim - 查看数组的维度数量
print(f"a1.ndim = {a1.ndim}")             # 3 → 三维数组
# 3. size - 查看数组的总元素个数
print(f"a1.size = {a1.size}")             # 24 → 2×3×4=24个元素
# 4. dtype - 查看数组的数据类型
print(f"a1.dtype = {a1.dtype}")           # int64（或int32）
# 5. itemsize - 查看每个元素占用的字节数
print(f"a1.itemsize = {a1.itemsize}")     # 8（int64占8字节）
# 6. nbytes - 查看数组占用的总字节数
print(f"a1.nbytes = {a1.nbytes}")         # 192 → 24×8=192字节
# 7. T - 转置（行变列，列变行，仅适用于二维及以上）
print(f"a1_2d.T = \n{a1.T}")

# 五、常用方法
# 1.修改形状 reshape() + arr.resize() + np.resize()

# 这里插入对视图的理解：
# 视图和原数组共用内存，两者内部元素协同改变

# resize和reshape的区别
# (1)元素个数要求
#     reshape要求的个数必须和原本的个数相等
#     而resize允许不等：
#         当多余时都是截断
#         当不足时 自动补0（arr.resize()） 或者 循环填充（np.resize()）
# (2)修改位置
#     reshape返回一个视图（优先视图）
#     arr.resize()修改原数组，在原地修改
#     np.resize()不修改原数组，返回独立副本

# reshape返回视图
# b=np.array([[1,2,3],[4,5,6],[7,8,9]])
b1 = b.reshape(1, 9)   # 重塑为1行9列
b2 = b.reshape(9,)     # 重塑为一维
b3 = b.reshape(3,-1)   # 相当于(3,3)，后面那个3自动计算出来。类似的，也可以是(-1,3)

# arr.resize()原地
b4=b.copy()
b5=b4.resize(3,3)

# np.resize()独立副本
b6=np.resize(b,(3,3))

# 2.展开一维之拷贝：
# 生成全新独立数组 b4，修改 b4 不会影响原数组 b
b7 = b.flatten()

# 3.展平一维之优先视图：
# 数组内存连续时，b5 和原数组 b 共用一块内存；修改 b5 会同步改动 b
# 只有数组内存不连续时，才被迫生成拷贝
b8 = b.ravel()

# 4.生成副本（不是同一块内存，相互独立，修改一者不影响另一者）
b9 = b.copy()
b9.resize(2, 5)    # 原地修改形状，不足补0

# 5.拼接和分割
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr_v = np.vstack((arr1, arr2))  # 垂直拼接（行增加）
arr_h = np.hstack((arr1, arr2))  # 水平拼接（列增加）
split_row = np.split(arr_v, 2, axis=0)  # 按行分割
split_col = np.split(arr_h, 2, axis=1)  # 按列分割
print("垂直拼接vstack：\n", arr_v)
print("水平拼接hstack：\n", arr_h)

# 六、索引方式
# 1.二维取数据方法：
# arr[i][j]         # 表示i行j列
# arr[i,j]          # 表示i行j列
# arr[i,[j,k]]      # 表示i行，j和k列
# 2.条件索引
# 取出所有 mask 为 True 位置对应的元素，筛选条件是元素值，和行列下标无关。
mask = b > 4
print("布尔索引b[b>4]：", b[mask]) # [5,6,7,8]
# 3.条件知识点扩充
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
mask = b > 4
print(mask)
# [[False False False]
#  [False  True  True]
#  [ True  True  True]]

# 七、数值运算
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

# 八、矩阵乘法
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



