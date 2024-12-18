from abc import ABC, abstractmethod

# Interface for Printable
class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass

# Interface for Calculable
class Calculable(ABC):
    @abstractmethod
    def calculate(self):
        pass

# Class that implements both interfaces
class Invoice(Printable, Calculable):
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def print_info(self):
        print(f"Item: {self.item}, Price: {self.price}")
    
    def calculate(self):
        return self.price * 1.1  # Adding a 10% tax

# Usage
invoice = Invoice("Laptop", 1000)
invoice.print_info()  # Output: Item: Laptop, Price: 1000
print(f"Total with tax: {invoice.calculate()}")