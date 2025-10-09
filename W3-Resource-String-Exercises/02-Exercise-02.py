# 2. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
#######################################################################################################################

a = int(input("Enter the value of integer a : "))
b = int(input("Enter the value of integer b : "))

flag = bool(input("Enter the boolean value for flag : "))

if ((a>=0) or (b>=0)) and flag==False:
    print("True")
elif ((a<0) and (b<0)) and flag==True:
    print("True")
else:
    print("False")