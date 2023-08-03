# # example function to add 2 number
# def anyname(a, b):
#     total = a + b
#     return total
#
# theoutput=anyname(4, 35)
# print(theoutput)

# example function to determine if given state has no sales tax
# def nosalestax(state):
#     stateswithnosalestax = ['AK', 'DE', 'MT', 'NH', 'OR']
#     # notax=None
#     if state.upper() in stateswithnosalestax:
#         return True
#         # notax=True
#     # return notax
#
# user_state = input()
# charge_tax = nosalestax(user_state)
# print(charge_tax)
#



def nosalestax(state):
    stateswithnosalestax = ['AK', 'DE', 'MT', 'NH', 'OR']
    if state.upper() in stateswithnosalestax:
        return True

user_input=input()
thetax=nosalestax(user_input)
print(thetax)