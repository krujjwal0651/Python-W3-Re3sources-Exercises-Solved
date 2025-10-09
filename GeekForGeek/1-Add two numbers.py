# 1. Write a Program to add two numbers
#######################################################################################################################


def add(num1, num2):
    return num1 + num2

num = (input("Enter two numbers to add them : ")).split(",")

print(f"The addition of {num[0]} and {num[1]} number is : {add(int(num[0]), int(num[1]))}  ")