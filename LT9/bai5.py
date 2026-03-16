class User:
    def __init__(self, ID):
        self.ID = ID

    def ID(self):
        '''Thuộc tính ID chỉ cho phép đọc.'''
        return self.ID

user1 = User('DSFWE143425')
print(f'User ID: {user1.ID}')
