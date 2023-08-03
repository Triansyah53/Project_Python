# Example 1
# main_number: int = 8
# while True:
#     User_number = int(input("Guess a number = "))
#     # print(type(main_number))
#     # print(type(User_number))
#     print(f"u entered {User_number}")
#     print(main_number != User_number)
#     if User_number == main_number:
#         break
# print('done')

# capitals={
#     "peru":"lima",
#     "philippines":"manila",
#     "spain":"madrid",
#     "ethiopia":"addis ababa",
#     "ghana":"accra"
# }
#
# user_input=input().lower()

# for countries,capital in capitals.items():
#     print(f"Current countery : {countries}")
#     if user_input == countries.lower():
#         print(f"Capital is {capital}")
#     continue
#     # break

# Example 3
# given a dictionary with book prices and list of courses, calculate total cost of books
book_prices = {"calculus": 300, "physics": 255, "chemistry": 400, "english": 150, "theater": 100}
my_courses = ["physics", "english", "psychology", "calculus", "history"]
total_cost = 0
for course in my_courses:
    if course not in book_prices.keys():
        continue
    total_cost += book_prices[course]
    total_cost = total_cost + book_prices[course]

print("Total books cost: {}".format(total_cost))


