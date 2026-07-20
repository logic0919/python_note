# Matplotlib 的大部分实用程序位于 pyplot 子模块下，并且通常使用 plt 别名导入：
import matplotlib.pyplot as plt
import numpy as np

# 1.plot()函数
'''
默认情况下，plot() 函数会从点到点绘制一条线。
该函数接受参数来指定图表中的点。
参数 1 是一个包含 x 轴上的点的数组。
参数 2 是一个包含 y 轴上的点的数组。
'''
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)

# 2.仅绘制点，用圆圈，没有线
plt.plot(xpoints, ypoints, 'o')

# 3.如果我们不指定 x 轴上的点，它们将根据 y 点的长度获得默认值 0, 1, 2, 3 等。
plt.plot(ypoints)

# 4.有线，并且点用圆圈/星表示
plt.plot(ypoints, marker = 'o')
plt.plot(ypoints, marker = '*')
# 以下代码执行逻辑：
#     先解析位置格式串 '*'：
#     简写串只有 marker 段 → 只画星标记、无线条；
#     再解析关键字 marker='x'：关键字参数优先级高于简写字符串，覆盖前面的标记样式。
#     最终效果：图像只有 x 标记，无连线，看不到星号*。
plt.plot(ypoints, '*',marker = 'x')
# plt.plot(ypoints, marker = 'x', '*') # 报错：位置参数必须全部写在关键字参数前面

# 5.'' 格式
# marker|line|color
# 保留零个：无|无|无：无点|实线|蓝色
# 保留一个的情况罗列：
# 保留第一个：marker|无|无：点|无线|黑
# 保留第二个：无|line|无：无点|实线|蓝
# 保留第三个：无|无|color：单独颜色无效，无法绘图
# 保留两个的情况罗列：
# marker|line|无：点|实线|蓝
# marker|无+color：点|无线|指定色
# 无+line+color：无点|实线|指定色
# 保留三个：marker|line|color：点|线|指定色
# plt.plot(ypoints, 'o:r') # 虚线+圆圈标记点+红色

# 这种情况下，无论linestyle是否指定都有线，这是和前面方式的区别之处
# maker=''|(ls)linestyle=''|color=''|(mec)markeredgecolor=''|(mfc)markerfacecolor=''|(lw)linewidth=''
# 保留零个：无|无|无：无点|实线|蓝色
# 保留一个的情况罗列：
# marker：marker|无|无：显示标记点|实线|蓝色
# line：无|line|无：无标记点|指定线型|蓝色
# color：无|无|color：无标记点|实线|指定颜色
# 保留两个的情况罗列：
# marker|line：marker|line|无：显示标记点|指定线型|蓝色
# marker|color：marker|无|color：显示标记点|实线|指定颜色
# line|color：无|line|color：无标记点|指定线型|指定颜色
# 保留三个：marker|line|color：显示标记点|指定线型|指定颜色

# 设定标记的大小：markersize 或者 ms
plt.plot(ypoints, marker = 'o', ms = 20)
# color：曲线线条、标记外圈边框共用色
# markeredgecolor：标记外圈边框，覆盖 color
# markerfacecolor：标记内部填充色，默认白色
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
# 还可以使用十六进制颜色值
plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')

# 6.多条线
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])
# 第一种：两条线在同一个函数里面
plt.plot(x1, y1, x2, y2)
# 第二种：两条线的函数分开
plt.plot(x1,y1)
plt.plot(x2,y2)

# 7.整张图的标题
plt.title("Sports Watch Data")
# 坐标轴的标签
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

# 8.标题和标签的字体属性
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

# 9.标题位置————合法值包括：'left'、'right' 和 'center'。默认值是 'center'。
plt.title("Sports Watch Data", loc = 'left')

# 10.网格线
# 默认both
plt.grid()
# 设定仅x轴
plt.grid(axis = 'x')
# 设定网格线的样式
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)


# 11.子图绘制
plt.subplot(1, 2, 1)
plt.plot(x1,y1)
plt.title("销售")

plt.subplot(1, 2, 2)
plt.plot(x2,y2)
plt.title("收入")

plt.suptitle("我的商店")
plt.show()

# 散点图
# 绘制的两个散点图在同一张图中，颜色不同，默认蓝色和橙色
x3 = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y3 = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x3, y3)
x4 = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y4 = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x4, y4)

# 设置颜色
plt.scatter(x3, y3, color = 'hotpink')

# 每个点不同的颜色
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
plt.scatter(x3, y3, c=colors)

# 彩色映射
# 'viridis' 是 Matplotlib 中可用的内置彩色映射之一。
# 此外，必须创建一个数组，其中包含值（从 0 到 100），每个散点图中的点一个值：
# 以下例子是均匀分配给0-200（根据数组中的最小值和最大值）
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 200])
plt.scatter(x3, y3, c=colors, cmap='viridis')
# 设定了最小和最大值，0-100
# 数组里大于 100 的数值，全部统一渲染成 vmax=100 对应的色标最大值颜色（viridis 最亮黄色）。
# 同理，小于 vmin=0 的数值，全部用色标最小值颜色（深紫色）。
plt.scatter(x3,y3,c=colors,cmap='viridis',vmin=0,vmax=100)
plt.colorbar()

# 绘制右侧 / 侧边颜色标尺（色条）
# 写上 plt.colorbar()：自动在画布侧边生成渐变色条，带数字刻度，直观看懂颜色代表的值。
plt.colorbar()

# 散点的大小
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
plt.scatter(x3, y3, s=sizes)

# 散点的透明度
plt.scatter(x3, y3, s=sizes, alpha=0.5)

# 条形图
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x,y)

# 水平条形图————barh()

# 设置颜色
plt.bar(x, y, color = "red")

# 条形宽度
# 注意：对于水平条形，请使用 height 而不是 width。
plt.bar(x, y, width = 0.1)
plt.barh(x, y, height = 0.1)

# 直方图
x = np.random.normal(170, 10, 250)
plt.hist(x)

# 饼形图
y = np.array([35, 25, 25, 15])
plt.pie(y)

# 可以设定每个楔形的标签
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels)

# 默认从x轴正方向逆时针开始转动
# 可以设定开始角度
plt.pie(y, labels = mylabels, startangle = 90)

# 如果指定了 explode 参数，并且不为 None，则它必须是一个数组，每个楔形一个值。
# 让其中一个楔形脱颖而出
myexplode = [0.2, 0, 0, 0]
plt.pie(y, labels = mylabels, explode = myexplode)

# 设定阴影
plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)

# 设定每个楔形的颜色
mycolors = ["black", "hotpink", "b", "#4CAF50"]
plt.pie(y, labels = mylabels, colors = mycolors)

# 展示图例
plt.legend()

# 带标签的图例
plt.legend(title = "Four Fruits:")

# 最后一句————绘制
plt.show()