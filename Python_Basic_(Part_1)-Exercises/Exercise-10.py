# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615
#######################################################################################################################

num = (input('Enter a number: '))

res = int(num) + int(num+num) + int(num+num+num)

print(f"Expected Result : {res}")

