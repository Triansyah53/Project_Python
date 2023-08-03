# # simple try catch
# try:
#     a = 5 / 0
# except:
#     print("dont do that")
#
# # example catch specific
# try:
#     b = 5 / 0
# except ZeroDivisionError:
#     print("u r something else")
#
# # example print the actual error
# try:
#     c = 5 / 0
# # except ZeroDivisionError as e
# except Exception as e:
#     print(f"the error is {e}")
#
# # example print multiple error
# try:
#     c = 5 / 0
#     b = {'name':'foo', 'age': 23}
#     x = b['school']
# # except ZeroDivisionError as e
# except (KeyError,ZeroDivisionError)  :
#     print(f"the error is")

# example print multiple error
# try:
#     c = 5 / 0
#     b = {'name':'foo', 'age': 23}
#     x = b['school']
# # except ZeroDivisionError as e
# except KeyError  :
#     print(f"the error is")
# except ZeroDivisionError:
#     print("zero ")

#Example raise an Exception
# y:
# a = 5 / 0
# print(foo)
# except Exception as e:
# print(f"error {e} has happened")
# raise ZeroDivisionError("foo bar")


#example re raise
try:
    a= 5/0
    print(foo)
except Exception as e:
    raise
