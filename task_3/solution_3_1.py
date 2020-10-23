# your code here
user_input = input()
alphabet = ""
for char in user_input:
    if char in alphabet:
        alphabet = alphabet + ""
    else:
        alphabet = alphabet + char
print(alphabet)
