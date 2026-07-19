''''''
'''
一、三种随机实现方式
    Python 标准内置库：import random
    NumPy 老式全局随机接口：np.random.xxx()
    NumPy 新版推荐生成器：rg = np.random.default_rng()，调用 rg.random() / rg.randint() 等
二、各自特点
    Python 内置 random 库
        仅能生成单个随机标量，无批量数组能力；
        批量生成需写循环，速度很慢；
        适用场景：简单脚本、少量随机取值。
    np.random 老式全局接口
        支持批量生成多维随机数组；
        全局共享随机状态，多线程容易冲突；
        属于遗留 API，新项目不推荐优先使用。
    NumPy Generator 生成器（rg）
        官方新标准，线程安全，每个生成器独立随机流；
        rg.random(shape) 生成 [0,1) 均匀分布数组，是批量随机首选；
        配套完整随机方法：rg.uniform / rg.normal / rg.randint / rg.choice；
        适用场景：机器学习、数值实验、大规模数组随机初始化。
'''