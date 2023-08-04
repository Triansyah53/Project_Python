class animal:
    def __init__(self,color,food_type=None):
        print("i am init")
        self.color=color
        self.food_type=food_type

    def move(self):
        print('animal move')

    def eat(self):
        print('animal eat')
        print(f'this animal eat {self.food_type}')

    def breath(self):
        print('animal breath')


my_animal=animal('blue','breakfast')
my_animal2=animal('red','lunch')
# print(my_animal)
# print(my_animal.color)
# print(my_animal2)
# print(my_animal2.food_type)
# print(type(my_animal))
# print(f'{my_animal.color} & {my_animal.food_type}')
# print(f'{my_animal2.color} & {my_animal2.food_type}')
print(my_animal.move())
print(f'my animal 1 eats {my_animal.food_type}')


