def fact(num: any):
    num = int(num)
    res=1
    while num > 0:
        res = res * num
        num = num - 1

    return res

x = input("Enter the num to calculate its factorial : ")

print(f"The Factorial of the {x} is : {fact(x)}" )
