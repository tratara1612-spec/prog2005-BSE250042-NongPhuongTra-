class Book:
    def __init__(self, name, price):
        self._name = name
        self._price = price
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        self._price = value


book_sample = Book("Python Cơ Bản", 150000)
print(f"Giá của đối tượng book_sample là: {book_sample.price}")
