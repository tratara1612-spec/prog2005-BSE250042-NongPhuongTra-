class Product:
    def __init__(self, price):
        self.price = price
    def price(self):
        return self.price
    def price (self, value):
        if value > 0:
            self.price = value
        else:
            print('Sản phẩm phải lớn không!')
            self.price = 0

    def __str__(self):
        return f"Product Information - Price: {self.price}"

test1 = Product(100)
test2 = Product(14)
test3 = Product(-23)

print(test1)
print(test2)
print(test3)
