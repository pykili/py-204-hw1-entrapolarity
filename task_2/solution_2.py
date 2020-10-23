# your code here
user_input = input()
most_frequent_character = ""
max = 0
for char in user_input:
  if user_input.count(char) > max:
    max = user_input.count(char)
    most_frequent_character = char
print(most_frequent_character)
