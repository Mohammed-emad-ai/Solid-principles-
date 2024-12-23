from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass

class Calculable(ABC):
    @abstractmethod
    def calculate(self):
        pass

class Invoice(Printable, Calculable):
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def print_info(self):
        print(f"Item: {self.item}, Price: {self.price}")
    
    def calculate(self):
        return self.price 

invoice = Invoice("Laptop", 1000)
invoice.print_info() 
print(f"Total : {invoice.calculate()}")
