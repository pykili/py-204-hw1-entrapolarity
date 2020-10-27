# your code here
user_input = input()
most_frequent_character = ""
max = 0
for char in user_input:
    count = 0
    for current_char in user_input:
        if current_char == char:
            count = count + 1
    if count > max:
        max = count
        most_frequent_character = char
print(most_frequent_character)
