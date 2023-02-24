class Student:

    def __init__(self):
        self.name = 'ivan'
        self.age = 18
        self.groupNumber = '10A'

    def get_name(self):
        print(f'Name: {self.name}')

    def get_age(self):
        print(f'Age: {self.age}')

    def get_group_number(self):
        print(f'Group Number: {self.groupNumber}')

    def set_name_age(self):
        self.name = 'no ivan'
        self.age = 25
        print(f'Name: {self.name}; Age: {self.age}')

    def set_group_number(self):
        self.groupNumber = '18C'
        print(f'Group Number: {self.groupNumber}')


a = Student()
a.get_name()
a.get_age()
a.get_group_number()
a.set_name_age()
a.set_group_number()
