"""
Write a program that takes an integer input and checks if it's even number.
Prints out 'True' if the number is even and 'False' if the number is not even.

e.g.4
Input: 2
Output: 2 is even

Input: 3
Output: 3 is not even
"""

number =input("ur number is = ")
if int(number) % 2 == 0:
    print("even")
else:print("odd")