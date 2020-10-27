# your code here
alphabet = ""
for smth in 'a'*10:
    user_input = input()
    for char in user_input:
        if (char in alphabet) == False:
            alphabet = alphabet + char
print(alphabet)
