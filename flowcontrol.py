#conditional statements example
x = -20
if x<0:
    print("Negative")
elif x%2 == 0:
    print("Positive Even")
else:
    print("Positive Odd")

#while loop
n = 5
i = 1
sum =0
while i <= n:
    sum = sum + i
    i = i + 1
print("Sum of first", n, "natural numbers is:", sum)

#for loop
str1 = "python"
for i in str1:
    print(i)
for i in range(10):
    print(i)