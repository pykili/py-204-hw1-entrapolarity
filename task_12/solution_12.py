# your code here
str = input()
occurred_twice = False
index = 0
for smth in "a"*(len(str) - 1):
    bigram = str[index] + str[index + 1]
    current_index = index
    count = 0
    for smth in "a"*(len(str) - index - 1):
        if str[index] == str[current_index]:
            if str[index + 1] == str[current_index + 1]:
                count = count + 1
        current_index = current_index + 1
    index = index + 1
    if(count > 1):
        occurred_twice = True
print(occurred_twice)
