# your code here
n = int(input())
num = 1
count = 0
sum = 0.0
for smth in "a"*n:
    if (num == 0) == False:
        num = int(input())
        sum = sum + num
        count = count + 1
average = sum / count
print(average)
