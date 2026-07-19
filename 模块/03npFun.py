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

# 四、形状和值都不确定
# 1.参照另一个矩阵的形状
b1=np.full((3,3), 6.6) # 指定形状填充同一个数字
m1=np.full_like(b1,7.7)
m2=np.zeros_like(m1)
m3=np.ones_like(m1)

# 四、常用属性
a1 = np.array([[[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]],
               [[13, 14, 15, 16],
                [17, 18, 19, 20],
                [21, 22, 23, 24]]])
# 1. shape - 查看数组的形状（各维度大小）
print(f"a1.shape = {a1.shape}")           # (2, 3, 4) → 2层，3行，4列
# 一维数组：np.array([1, 2, 3])                              (3, )
# 行向量：np.array([[1, 2, 3]])                              (1, 3)
# 列向量：np.array([[1], [2], [3]])                          (3, 1)
# 矩阵：np.array([[1,2],[3,4]])                              (2, 2)
# 三维数组：np .ar ray ([[[1,2],[3,4]], [[5,6],[7,8]]])       (2, 2, 2)
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

# 扩展：flat迭代器：di.flat
d1 = np.array([[1,2,3],[4,5,6]])
# 索引取值（像一维数组一样访问）
d2 = d1.flat[0]
d3 = d1.flat[4]
print(d2, d3)  # 1 5
# 索引批量赋值（原地修改原数组）
d1.flat[1::2] = 0
print(d1)
# [[1 0 3]
#  [0 5 0]]
# for循环遍历全部元素
for val in d1.flat:
    print(val, end=" ")
# 转成完整一维数组（搭配list）
d4 = list(d1.flat)
print(d4)

# 4.生成副本（不是同一块内存，相互独立，修改一者不影响另一者）
b9 = b.copy()
b9.resize(2, 5)    # 原地修改形状，不足补0

# 5.拼接和分割
# 函数：np.vstack()+np.hstack()+np.split()
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr_v = np.vstack((arr1, arr2))  # 垂直拼接（行增加）
arr_h = np.hstack((arr1, arr2))  # 水平拼接（列增加）
split_row = np.split(arr_v, 2, axis=0)  # 按行分割，上下分割成两份
split_col = np.split(arr_h, 2, axis=1)  # 按列分割，左右分割成两份

# 六、索引方式
# 1.二维取数据方法：
# arr[i][j]         # 表示i行j列
# arr[i,j]          # 表示i行j列
# arr[i,[j,k]]      # 表示i行，j和k列

# 2. ...的使用：
# 作为替代掉多个连续的完整切片，例如对于五维[::,::,::,2,3]也就是[:,:,:,2,3]可以替换为[...,2,3]
# 三维数据
e1 = np.random.randint(1, 10, size=(2, 3, 4))
print(e1)
# 只确定一个维度，所以剩下的维度数是3-1=2
e2 = e1[..., 2]
print("e2 shape：", e2.shape)  # (2, 3)
print("e2：", e2)
# 只确定一个维度，所以剩下的维度数是3-1=2
e3 = e1[0, ..., 1:4]
print("e3 shape：", e3.shape) # (3, 3)
print("e3:", e3)
# 确定两个维度，所以剩下的维度数是3-2=1
e4 = e1[1, 2, ...]
print("e4 shape：", e4.shape) # (4,)
print("e4：", e4)

# 3.条件索引
# 取出所有 mask 为 True 位置对应的元素，筛选条件是元素值，和行列下标无关。
mask = b > 4
print("布尔索引b[b>4]：", b[mask]) # [5,6,7,8]

# 4.条件知识点扩充
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
mask = b > 4
print(mask)
# [[False False False]
#  [False  True  True]
#  [ True  True  True]]

# 5.切片
# [:]：只有一个冒号的情况下省略的是第二个冒号也就是默认步长为1
# [::]：默认全部
# [::-1]：反转

# 6.ix_()
h1 = np.arange(12).reshape(3,4)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
# 需求：提取第0、2行，第1、3列
rows = [0,2]
cols = [1,3]
# 直接写：只会取 (0,1)、(2,3) 两个对角点，不是整块区域
h2 = h1[rows, cols]
print(h2)  # [1 11]
# 原因：numpy 把两个列表一一配对，只取一一对应的坐标，不取全部交叉组合。
h3 = h1[np.ix_(rows, cols)]
print(h3)
# [[ 1  3]
#  [ 9 11]]

# 7.其他
b[b>5] = 0 # 所有大于5的元素改为0
b[1,:] = -1 # 整行赋值

# 七、数值运算
add_arr = b + 2
sub_arr = b - 1
mul_arr = b * 3
div_arr = b / 2
pow_arr = b ** 2
sqrt_arr = np.sqrt(b)
mod_arr = b % 2

# 八、矩阵乘法
# 1.*：对应位置数字单独相乘
mat_mul1 = b * b

# 2.@：线性代数中的矩阵相乘，行列匹配原则
# 2.1.两个二维矩阵：线性代数
# 2.2.先总述对于一个二维矩阵和一个一维数组@的结果
#         以下只是算数逻辑上的等效而非实际原理
#         二维矩阵是mn，但一维数组只能是m1或者1m，
#         所以为了配合矩阵乘法规则，若是一维数组在前面，则依然是看成1m，那么后面必须是mn，
#         若是一维数组在后面，则看成m1，前面则必须是nm，
#         那么此时相乘的结果分别是1n和n1，
#         然后将其都转为一维数组，也就是1n，并且注意不是矩阵形式而是一维数组形式，也就是只有一个中括号。
# 2.3.一个mn二维矩阵和一个长度为n（形如1n的二维矩阵）的一维数组：
#     看成mn的二维矩阵和n1的二维矩阵，所得为m1的二维矩阵转置之后也就是1m的二维矩阵转为一维数组的结果，
#     也就是(m,)，也就是长度为m的一维数组
#         示例代码：
#         # 左矩阵：3行2列
#         a = np.array([[1, 2],
#                       [3, 4],
#                       [5, 6]])
#         b = np.array([10, 20])
#         c=np.array([[10],[20]])
#         # 矩阵 @ 一维数组
#         re1 = a @ b
#         print(re1)
#         # 矩阵 @ 矩阵
#         re2=a@c
#         print(re2)
#         mat_mul2 = b @ b.T
# 2.4.一个长度为m的一维数组和一个mn，也就是(m,)@(m,n)
#         示例代码：
#         # 一维数组：1行4列
#         a = np.array([1, 2, 3, 4])
#         # 二维矩阵：1行4列
#         b = np.array([[1, 2, 3, 4]])
#         # 矩阵：4行2列
#         c = np.array([
#             [1, 2],
#             [3, 4],
#             [5, 6],
#             [7, 8]
#         ])
#         re1=a@c
#         re2=b@c
#         print(re1) # [50 60]
#         print(re2) # [[50 60]]
# 2.5.两个一维数组相乘：
#     若是长度相等：做内积得一个标量数组
#     若是长度不相等：报错
# 2.6.高维
#     三维：（二维无批次，从三维开始才有批次）
#         计算方法：
#             把最后两维当作矩阵，前面的所有维度都作为批次（Batch），进行“对应批次”的矩阵乘法。
#             广播：两种情况，分别是a=d或者a=1或者d=1，三种情况分别得到abe或者dbe或者abe
#                 (b,m,n) @ (b,n,p) → (b,m,p) —— 批次维度相同，一对一对应。
#                 (b,m,n) @ (1,n,p) → (b,m,p) —— 右矩阵批次为1，广播到左矩阵的批次。
#                 (1,m,n) @ (b,n,p) → (b,m,p) —— 左矩阵批次为1，广播到右矩阵的批次。
#                 (b,m,n) @ (c,n,p) —— 若 b ≠ c 且均不为1，则报错。
#     四维：
#         (a,b,m,n) @ (a,b,n,p) → (a,b,m,p)
#         (a,1,m,n) @ (1,b,n,p) → (a,b,m,p)
# 2.7.标量乘一个一维向量
#     @不支持所有标量相乘，所以报错
# 2.8.标量乘一个二维矩阵
#     同上

# 3.np.matmul()：等价于@

# 4.np.dot()：
#     像以上2.2-2.5的情况，这两种运算结果一样。只有涉及到三维以及更高维度时才不一样。
#     另外，对于带有标量的乘法，就是逐元素都乘这个矩阵，对于一维数组、二维矩阵甚至高维都是这样

# 总结一下：
    # 对于有标量的乘法，用*
    # 对于无标量的，二维及以下的，@和dot结果一样，所以用dot
    # 这么看来，dot不用学，而且dot的高维很奇葩，项目中几乎不使用
mat_mul3 = np.dot(b, b.T)

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

# 十、数学相关
c1 = np.array([1, 2, 3, 4])
# 指数运算
c2 = np.exp(c1)         # e^x
c3 = np.exp2(c1)        # 2^x
c4 = np.exp10(c1)       # 10^x
# 对数运算
c5 = np.log(c1)         # ln(x)
c6 = np.log2(c1)        # log2(x)
c7 = np.log10(c1)       # log10(x)

# 弧度数组 c8
c8 = np.array([0, np.pi/2, np.pi])
# 三角函数
c9 = np.sin(c8)
c10 = np.cos(c8)
c11 = np.tan(c8)

# 反三角函数输入数组 c12
c12 = np.array([0, 1])
# 反三角函数
c13 = np.arcsin(c12)
c14 = np.arccos(c12)
c15 = np.arctan(c12)

# 角度数组 c16
c16 = np.array([0, 90, 180])
c17 = np.rad2deg(c8)    # 弧度转角度
c18 = np.deg2rad(c16)   # 角度转弧度

# 正负浮点数组 c19
c19 = np.array([-1.2, 3.4, -5, 1.9, -2.1])
c20 = np.abs(c19)       # 绝对值
c21 = np.floor(c19)     # 向下取整
c22 = np.ceil(c19)      # 向上取整
c23 = np.round(c19)     # 四舍五入

# 平方、开方、幂次
c24 = np.square(c1)
c25 = np.sqrt(c1)
c26 = np.power(c1, 3)

# 另外还有np.add()等

# reduce运算
g1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# 沿axis=0累加，等价 np.sum(e1,axis=0)
g2 = np.add.reduce(g1, axis=0)
g3 = np.multiply.reduce(g1, axis=1)
print(g1)
print(g2)
print(g3)

# 十一、axis的使用
# axis=0：竖着算
# axis=1：横着算
# 0v1h
f1 = np.array([[1, 2], [3, 4]])
f2 = np.array([[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12]])

# 拼接 hstack/vstack/dstack/concatenate
f3 = np.vstack((f1, f1))
f4 = np.hstack((f1, f1))
# np.concatenate((数组1, 数组2, 数组3...), axis=拼接维度)

# 分割 hsplit/vsplit/split/array_split
# split(axis=0) 等价 vsplit，按行均分2份
f5 = np.split(f1, 2, axis=0)
# split(axis=1) 等价 hsplit，按列均分2份
f6 = np.split(f1, 2, axis=1)
# split 指定分割点 [1,2]
f7 = np.split(f1, [1,2], axis=0) # 划分垂直方向。在下标为1和下标为2的前面分别画一条线
# array_split 支持无法均分，3行切2份
f8 = np.array_split(f2, 2, axis=0)

# 求和运算，用f1作为求和数组
f9 = np.sum(f1, axis=0)  # 按列求和
f10 = np.sum(f1, axis=1) # 按行求和

# 打印输出
print("f5：", f5)
print("f6：", f6)
print("f7：", f7)
print("f8：", f8)
print("f9：", f9)
print("f10：", f10)

# 十二、搜索where()和searchsorted()
# where()返回满足条件的下标
# searchsorted()：传入的数组必须是升序递增的，然后将传入的要插入的值放在合适的位置，使得继续升序递增
i1 = np.array([1, 2, 3, 4, 5, 4, 4])
i2 = np.where(i1 == 4)
print(i2)  # 输出：(array([3, 5, 6]),)
# 第二段 searchsorted 二分定位
i3 = np.array([6, 7, 8, 9])
i4 = np.searchsorted(i3, 7)
print(i4)  # 输出：1

# 十三、排序
# 1.np.sort () —— 返回新排序数组（不修改原数组）
j1 = np.array([3,1,4,1,5])
j2 = np.sort(j1)
print(j1)  # [3 1 4 1 5] 原数组不变
print(j2)  # [1 1 3 4 5] 升序新数组

# 降序
j3 = np.sort(j1)[::-1]
print(j3)  # [5 4 3 1 1]

# 多维按轴排序
j4 = np.array([[3,1],[2,4]])
j5 = np.sort(j4, axis=0) # 按列排序
j6 = np.sort(j4, axis=1) # 按行排序
print(j5)
print(j6)

# arr.sort () —— 原地排序（直接修改原数组，无返回值）
j1.sort()

# 十四、过滤
k1 = np.array([61, 62, 63, 64, 65])
k2 = [True, False, True, False, True]
k3 = k1[k2]
print(k3)  # 输出：[61 63 65]

k4 = np.array([61, 62, 63, 64, 65])
k5 = k4 > 62
k6 = k4[k5]
# 或者以上代码直接写成 k6 = k4[k4>62]
print(k5)  # 输出：[False False  True  True  True]
print(k6)  # 输出：[63 64 65]

# 十五、数组基本操作————增删改查
m1 = np.array([10, 20, 30, 40])
# 增：append末尾追加
m2 = np.append(m1, [50, 60])
print("末尾新增：", m2)  # [10 20 30 40 50 60]
# 增：insert指定位置插入
m3 = np.insert(m1, 2, [22, 24])
print("指定位置插入：", m3)  # [10 20 22 24 30 40]
# 删：delete删除指定下标
m4 = np.delete(m1, [1, 3])
print("删除下标1、3：", m4)  # [10 30]

# 十六、zip()
import numpy as np
l1 = [1, 2, 3, 4]
l2 = [4, 5, 6, 7]
l3 = []
for l4, l5 in zip(l1, l2):
  l3.append(l4 + l5)
print(l3)  # [5, 7, 9, 11]
l6 = np.add(l1, l2)
print(l6) # [ 5  7  9 11]
