# Armstrong Number : It is a number that is equal to the sum of cubes of its digits.
# e.g 153 is an Armstrong Number as (1*1*1 + 5*5*5 + 3*3*3 = 153).
# e.g 120 is not an Armstrong Number as (1*1*1 + 2*2*2 + 0*0*0 = 9)
#######################################################################################################################

def check_armstrong_number(num: str):
    res = 0
    for i in num:
        res = res + (int(i) ** 3)

    if res == num:
        return "Its an Armstrong Number."
    else:
        return "It is not an Armstrong Number."


num = input("Enter a number to check if it is an Armstrong Number : ")
print(check_armstrong_number(num))

