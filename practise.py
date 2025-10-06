from abc import ABC , abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print('it is working')


#com = Computer()
com = Laptop()
com.process()