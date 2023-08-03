# infinity loop
# myvar= True
# while myvar:
#     print("abc")

# counter=1
# while counter <=10:
#     print(counter)
#     counter=counter+1
#     if counter > 10:
#         print("stop")

# main_number = 8
# User_number = 0
# while main_number != User_number:
#     User_number = input()
#     if User_number.isdigit():
#         print("ur input is digit")
#     else:
#         print("blank")

main_number = 8
User_number = 0
while User_number != main_number:
    User_number = int(input())
    # print(type(main_number))
    # print(type(User_number))
    print(f"u entered {User_number}")
    print(main_number != User_number)
print('done')