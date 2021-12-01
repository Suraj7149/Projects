class Item:
    def __init__(self, name: str, price: float, quantity = 0):

        assert price > 0, f"Price {price} must be greater than 0."
        assert quantity > 0, f"quantity {quantity} must  be greater than 0."
        
        self.name = name
        self.price = price
        self.quantity = quantity

    def turn_over(self):
        return self.price*self.quantity



item1 = Item("Phone", 200, 500)
print(item1.turn_over())

item2 = Item("Laptop", 700, 1000)
print(item2.turn_over())