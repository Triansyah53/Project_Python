class animal:
    def __init__(self,color,food_type=None):
        # print("i am init")
        self.color=color
        self.food_type=food_type

    def move(self):
        print('animal move')

    def eat(self):
        print('animal eat')
        print(f'this animal eat {self.food_type}')

    def breath(self):
        print('animal breath')


class Cat(animal):
    def __init__(self,color,food_type,name,breed):
        super().__init__(color,food_type)
        self.name=name
        self.breed=breed

    def cat(self):
        print('meow')

class Dog(animal):
    def __init__(self,color,food_type,name,breed):
        super().__init__(color,food_type)
        self.name=name
        self.breed=breed

    def woof(self):
        print('woof..')

    def as_security(self):
        print('My dog is my home security')


mydog=Dog('brown','meat','max','shiba')
print(f'{mydog.color} {mydog.name} {mydog.breed}')
mydog.eat()


# mycat=Cat('udon','mainecoon')
# print(f'{mycat.name} {mycat.breed}')
# mycat.eat()

