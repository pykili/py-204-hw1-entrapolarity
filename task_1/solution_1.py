# your code here
a = input()
nums = "9876543210"
ans = ""
for num in nums:
  if num in a:
    ans = ans + num 
print(ans[0])
