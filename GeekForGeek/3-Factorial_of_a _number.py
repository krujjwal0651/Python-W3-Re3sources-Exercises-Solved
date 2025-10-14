def fact(num: any):
    num = int(num)
    res=1
    while num > 0:
        res = res * num
        num = num - 1

    return res


def fact2(num: any):
    num = int(num)
    res = 1

    for i in range (1, num+1):
        res = res * i
    return res




x = input("Enter the num to calculate its factorial : ")

print(f"The Factorial of the {x} is : {fact(x)}" )

print(fact2(x))
