mylist = [10,12,16,19,25,30,35,40,45,50]
#looping through list using for loop
sum = 0
for item in mylist:
    sum += item
print("Sum of all items in the list is:", sum)
average = sum / len(mylist)
print("Average of items in the list is:", average)
print(f"-----------------------------------")
for i in range(len(mylist)):
    print(f"Item at index {i} is {mylist[i]}")
print(f"-----------------------------------")
for val in range(6):
    print("Current value:", val)
print(f"-----------------------------------")
#while loop format
a = 0
while a < 5:
    print("Value of a is:", a)
    a += 1

value = 0
tot = 0
while value <= 10:
    tot += value
    value += 1
print("Total sum from 0 to 10 is:", tot)

for k in mylist:
    if k == 25:
        print("25 is found in the list, stopping the loop")
        break
    print(k)

for num in range(5):
    num = int(input("Enter a number: "))
    if num < 0:
        print("Negative number entered, skipping to next iteration")
        break
    else:
        print("You entered:", num)
str1 = "datascience"
for ch in str1:
    print(ch)
    if ch == "s":
        print("Character 's' found, skipping the loop")
        continue
