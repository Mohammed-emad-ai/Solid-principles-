class Order:
    def __init__(self, items, quantities, prices):
        self.items = items
        self.quantities = quantities
        self.prices = prices

    def total_price(self):
        return sum(q * p for q, p in zip(self.quantities, self.prices))

class OrderPrinter:
    @staticmethod
    def print_order(order):
        print("Order Details:")
        for item, quantity, price in zip(order.items, order.quantities, order.prices):
            print(f"Item: {item}, Quantity: {quantity}, Price per Unit: {price}")
        print(f"Total Price: {order.total_price()}")

class OrderSaver:
    @staticmethod
    def save_to_file(order, filename):
        with open(filename, "w") as file:
            file.write("Order Details:\n")
            for item, quantity, price in zip(order.items, order.quantities, order.prices):
                file.write(f"Item: {item}, Quantity: {quantity}, Price per Unit: {price}\n")
            file.write(f"Total Price: {order.total_price()}\n")

order = Order(["Apple", "Banana", "Orange"], [3, 5, 2], [2.5, 1.2, 3.0])
OrderPrinter.print_order(order)
OrderSaver.save_to_file(order, "order.txt")  