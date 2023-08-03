import random
exp=random.randint(100,200)
exp2=random.randrange(30)
print(exp)
print(exp2)

my_list=['aaa','bbb','ccc','ddd','eee']
exp3=random.shuffle(my_list)
print(my_list)

exp4=random.choice(my_list)
print(exp4)

exp5=random.sample(my_list,3)
print(exp5)