# Matplotlib 的大部分实用程序位于 pyplot 子模块下，并且通常使用 plt 别名导入：
import matplotlib.pyplot as plt
import numpy as np

# plot()函数
'''
默认情况下，plot() 函数会从点到点绘制一条线。
该函数接受参数来指定图表中的点。
参数 1 是一个包含 x 轴上的点的数组。
参数 2 是一个包含 y 轴上的点的数组。
'''
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)

# 仅绘制点，用圆圈，没有线
plt.plot(xpoints, ypoints, 'o')

# 如果我们不指定 x 轴上的点，它们将根据 y 点的长度获得默认值 0, 1, 2, 3 等。
plt.plot(ypoints)

# 有线，并且点用圆圈/星表示
plt.plot(ypoints, marker = 'o')
plt.plot(ypoints, marker = '*')

# '' 格式
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

# maker=''|line=''|color=''
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







plt.show()