# 6.Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')
#######################################################################################################################

num = (input('Enter comma-seperated numbers: '))

lst = num.split(',')

tup = tuple(lst)

print(f"\nList : {lst} \nTuple : {tup}")

### The list and Tuples printing above are String type. If we need int type of List and Tuple then :

int_lst = [int(x) for x in lst]
int_tup = tuple(int_lst)
print(f"\nInt List : {int_lst} \nInt Tuple : {int_tup}")
