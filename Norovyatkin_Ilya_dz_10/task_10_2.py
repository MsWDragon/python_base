from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calculate(self):
        pass

    def __str__(self):
        return str(self.param)
        
class Coat(Clothes):

    @property
    def calculate(self):
        return float('{:.2f}'.format(self.param / 6.5 + 0.5)) 

class Costume(Clothes):

    @property
    def calculate(self):
        return float('{:.2f}'.format(self.param * 2 + 0.3))


if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)

    print(coat.calculate)  # 7.42
    print(costume.calculate)  # 6.3
