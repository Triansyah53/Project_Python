# my_list = ['book', 'boat', 'water', 'tissue']
# for i in my_list:
#     print(i)
#     print('------')
#
# for j in reversed(my_list):
#     print(j)
#     print('------')

#example 2

# quote="if u dont believe in ur self, then who will"
# convet = quote.split()
# for i in quote.split():
#     if len(i)<= 3:
#         print(i)
#     else:pass
#
#example 3

quote="if u dont believe in ur self, then who will"
empty=[]
for i in quote.split():
    if len(i)<=3:
        empty.append(i)
        # print(empty)
print(empty)
print(' '.join(empty))

#assignment loop empty list

empty2=[]
for j in empty2:
    print(j)
