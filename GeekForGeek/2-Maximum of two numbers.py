# 2. Write a Program to find maximum of two numbers
#######################################################################################################################


def maxm(num1: any , num2: any):
    num1 = int(num1)
    num2 = int(num2)
    if int(num1) > int(num2):
        return f"{num1} is greater than {num2}"
    elif int(num2) > int(num1):
        return f"{num2} is greater than {num1}"
    else:
        return "Both are Equal"

#----

num = input("Enter the two numbers to find maximum of them :  ").split(" ")

res = maxm(num[0],num[1])
print(res)
