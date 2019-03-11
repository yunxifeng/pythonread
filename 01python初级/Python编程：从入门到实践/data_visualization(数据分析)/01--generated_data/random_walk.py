from random import choice

class RandomWalk():
    """一个生成随机漫步数据的类"""
    # 这个类需要三个属性
    # 1.存储随机漫步次数的变量
    # 2.存储随机漫步经过的每个点的x坐标构成的列表
    # 3.存储随机漫步经过的每个点的y坐标构成的列表
    # 这个类只包含两个方法
    # 1.__init__(): 初始化随机漫步的属性
    # 2.fill_walk(): 计算随机漫步经过的所有点

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points
        # 所有随机漫步都始于(0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        # 不断漫步, 直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进的方向以及沿这个方向前进的距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
