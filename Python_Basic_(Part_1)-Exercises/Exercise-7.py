# 7. Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java
#######################################################################################################################

file_name = input('Enter file name: ')

extn = file_name.split('.')     # extn will be list type

# print(type(extn))

print(f"The extension of file name entered by you is: {extn[-1]}") # we can use -1 to print last index of a list

