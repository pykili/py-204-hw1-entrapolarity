# your code here
sum = 0
n = 0
ans = True
for smth in "a"*100:
    n = n + 1
    sum = sum + 2 * n - 1
    if (n * n == sum) == False:
        ans = False
print(ans)
