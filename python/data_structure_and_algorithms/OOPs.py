import csv
class Item:
    pay_rate = 0.8 #20% dicount
    all = []

    def __init__(self, name: str, price: float, quantity = 0):

        assert price > 0, f"Price {price} must be greater than 0."
        assert quantity > 0, f"quantity {quantity} must  be greater than 0."
        
        self.__name = name
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)
    

    @property
    def name(self):
        return self.__name
    @property
    def price(self):
        return self.__price

    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
        print(f"New name of the class's instance is {self.name}")

    @price.setter
    def price(self, new_price):
        self.__price = new_price
        print(f"New price of the object is {self.__price}")
    def turn_over(self):
        return self.__price*self.quantity

    @classmethod
    def intantiate_from_csv(cls):
        with open("G:\\Projects\\python\\data_structure_and_algorithms\\items.csv", "r") as i:
            reader = csv.DictReader(i)
            items = list(reader)

            

        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity")),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            False

    def __repr__(self):
        return f"Item('{self.name}, {self.__price}, {self.quantity}')"

    # read only attribute 
    @property
    def read_only_name(self):
        return "AAA"

    def __connect(self, smpt_server):
        pass

    def prepare_body(self):
        return f"""
        Hello Someone.
        {self.name} Here,  I just wanna say
        I am motivated!!!."""

    def __send():
        pass
    
    def send_mail(self):
        self.__connect()
        self.prepare_body()
        self.__send()

    



# item1 = Item("Phone", 200, 500)
# # print(item1.turn_over())

# item2 = Item("Laptop", 700, 1000)
# # # print(item2.turn_over())

# Item.intantiate_from_csv()
# print(Item.all)

# print(Item.is_integer(7))

# for instance in Item.all:
#     print(instance)



