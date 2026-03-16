class Product():
    def __init__(self, price):
        self.price = price

    def price(self):
        return self.price
    def price(self, value):
        if value > 0:
            self.price = value
        else:
            print('Giá phải lớn hơn 0!')

    def __str__(self):
        return str(self.price)

p = Product(100)
print(p)
