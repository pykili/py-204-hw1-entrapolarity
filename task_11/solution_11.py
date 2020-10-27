# your code here
left = input()
right = input()
ans = False
index_right = 0
if len(left) <= len(right):
    for smth in "a"*(len(right) - len(left) + 1): #оператор in используется только в записи цикла
        count = 0
        index_left = 0
        current_index_right = index_right
        for smth in "a"*len(left):
            if left[index_left] == right[current_index_right]:
                count = count + 1
            index_left = index_left + 1
            current_index_right = current_index_right + 1
        if count == len(left):
            ans = True
        index_right = index_right + 1
print(ans)
