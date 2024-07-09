import matplotlib.pyplot as plt
import numpy as np
import random


class player:
    def __init__(self):
        self.choice = [0, 0]
        self.choice[0] = random.randint(0, 10)
        self.choice[1] = 10 - self.choice[0]
        self.temp_chiose = 0

    def get_chiose(self):
        if self.choice[0] == self.choice[1]:
            self.temp_chiose = random.choice([0, 1])
            return self.temp_chiose
        
        temp = self.choice[0] + self.choice[1]
        if temp <= 0:
            self.temp_chiose = random.choice([0, 1])
            return self.temp_chiose

        temp = random.randint(0, temp)
        if temp <= self.choice[0]:
            self.temp_chiose = 0
            pass
        else:
            self.temp_chiose = 1
            pass
        return self.temp_chiose

    def evaluate_chiose(self, evaluate):
        self.choice[self.temp_chiose] += evaluate

    def __lt__(self, other):
        # 定义小于比较逻辑

        return self.choice[0] + self.choice[1] < other.choice[0] + other.choice[1]


def game121(A: player, B: player):
    evaluate = [[(-1, -1), (2, 0)], 
                [(0, 2), (1, 1)]]
    temp = evaluate[A.get_chiose()][B.get_chiose()]
    A.evaluate_chiose(temp[0])
    B.evaluate_chiose(temp[1])





if __name__ == "__main__":
    players = []

    for _ in range(1024):
        players.append(player())
        pass
    players_size=len(players)
    y1=[]
    y2=[]
    y3=[]
    for ttt in range(1,1024 * 64):
        random.shuffle(players)
        n = players_size // 2
        for i in range(n):
            game121(players[i], players[i + n])
            pass
        Asize=0
        Bsize=0
        for p in players:
            Asize+=p.choice[0]
            Bsize+=p.choice[1]
            pass
        tem=Asize+Bsize
        y1.append(tem/players_size/ttt)
        P=Asize/tem
        y2.append((P)*10)
        y3.append((1-P)*10)
        pass

    x=range(len(y1))
    # 绘制折线图  
    plt.plot(x, y1, label='Line 1',color='green', linestyle='--')  

    plt.plot(x, y2, label='Line 2',color='red')  

    # 如果需要，可以添加更多线  

    plt.plot(x, y3, label='Line 3',color='blue')  # 使用虚线样式  

   
    
    # 添加标题和轴标签  
    plt.title('Simple Plot')  
    plt.xlabel('x axis label')  
    plt.ylabel('y axis label')  
    
    # 显示图表  
    plt.show()


