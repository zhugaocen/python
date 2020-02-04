class PanCake():
    def __init__(self):
        self.cookedString = '生的'
        self.cookedLevel = 0
        self.zuoliao = []

    def __str__(self):
        return "煎饼的状态：{}，烤了的时间：{}，作料是：{}".format(
            self.cookedString, self.cookedLevel, self.zuoliao)

    def cook(self, cooked_time):
        self.cookedLevel += cooked_time
        if self.cookedLevel >= 0 and self.cookedLevel <= 3:
            self.cookedString = '生的'
        elif self.cookedLevel > 3 and self.cookedLevel <= 5:
            self.cookedString = '半生不熟'
        elif self.cookedLevel > 5 and self.cookedLevel <= 8:
            self.cookedString = '熟了'
        else:
            self.cookedString = '焦了'

    def add_zuoliao(self, food):
        self.zuoliao.append(food)
        

jb = PanCake()
jb.cook(1)
jb.cook(1)
jb.cook(1)
jb.cook(1)
jb.add_zuoliao('火腿')
print(jb)
