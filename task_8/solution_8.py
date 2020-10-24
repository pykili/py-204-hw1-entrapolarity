# your code here
n = int(input())
num = 1
count = -1 #не считаем 0 элементом последовательности
sum = 0.0
for smth in "a"*(n + 1): #могут вводиться N чисел, а потом 0
    if (num == 0) == False:
        num = int(input())
        sum = sum + num
        count = count + 1
average = sum / count
print(average)
