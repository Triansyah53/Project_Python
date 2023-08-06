"""
Create a class that has basic calculating functions.

You can have as many methods as you like but here are few suggestions.
* method to take two numbers and add them and return the sum
* method to take two numbers and subtract the second number from the first number and return the diff
* method to take two numbers and return the multiplication of the two
* method to divide two numbers and return the result (first number divided by second number)

"""


class Calculator():
    def addition(self, x, y):
        return x + y

    def substraction(self, x, y):
        return x - y

    def multlipication(self, x, y):
        return x * y

    def division(self, x, y):
        return x / y


num1 = float(input('Enter number 1 : '))
num2 = float(input('Enter number 2 : '))
calculator = Calculator()
result = calculator.substraction(num1, num2)
print(result)


# calculator=Calculator()
# result=calculator.substraction(4,5)
# print(result)
