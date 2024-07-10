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
