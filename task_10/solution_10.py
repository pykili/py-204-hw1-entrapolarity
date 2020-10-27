# your code here
str = input()
is_palindrom = False
str1 = ""
for char in str:
    str1 = char + str1
if str == str1:
    is_palindrom = True
print(is_palindrom)
