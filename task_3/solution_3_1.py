# your code here
user_input = input()
alphabet = ""
for char in user_input:
    if (char in alphabet) == False:
        alphabet = alphabet + char
print(alphabet)
