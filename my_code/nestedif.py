theater_name="xyz"
rated=17

print(f"Welcome to {theater_name} !")

user_input = input("enter ur age = ")
print(user_input)

if int(user_input) > rated:
    print("Enjoy the movie")
else:
    adult_present = input("do u have an adult companying u? YES/NO")
    if adult_present.lower() == "YES":
        print("aight fineee")
    else:
        print("GTFO")