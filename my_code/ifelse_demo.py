# a=111
# b=5
# c=30
# d=10
#
# if a < b:
#     print("tes \n tes")
# elif a>b and c>b :print("haha")
# else:print("false")

shows = ["Friends", "The Office", "Breaking Bad", "Stranger Things"]
movies = ["Rocky", "Jaws", "Batman", "Wonder Woman"]

my_choice='Friends'

if my_choice in shows or movies:
    print("true")
else:("false")

if my_choice in shows:
    print("ur choice is a show")
elif my_choice in movies:
    print("ur choice is a movies")
else:print("idk")