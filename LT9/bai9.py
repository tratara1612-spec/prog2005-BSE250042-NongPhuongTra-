class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print(f'Chú chó {self.name} đang sủa: Gâu Gâu!')

cho = Dog('Mèo')
print(f'Tên chó: {cho.name}')
cho.sound()
