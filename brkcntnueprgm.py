mylist = [123, 124, 545, 612, 274, 128, 129, 130]
for item in mylist:
    print(item)
    if item == 612:
        break
print("break statement")

for i in range(5):
    n = float(input("Enter the Number:"))
    if n < 0:
        print("Negative is arrived")
        break
    else:
        print("Value of n is:", n)

str1 = 'Python'
for name in str1:
    if name == 't':
        continue
    print(name)

print("__________________________________________________________________")
for j in range(1, 11):
    if j == 6:
        continue
    print(j)

print("------------------------------------------------------------------------------")

a = 0
while a < 10:
    a += 1
    if a == 3:
        continue
    print(a)
