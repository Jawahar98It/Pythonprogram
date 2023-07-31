mylist = [10, 20, 30, 50, 70]
for i in mylist:
    print(i)

sum = 0
print("Adding all values in list")
for j in mylist:
    sum += j

print(sum)
print("---------------------------------------------------")
for n in range(6):
    print(n)

print("================================================")

for n1 in range(0, 6):
    print(n1)

print("-----------------------------------------------")

for x in range(0, 8, 2):
    print(x)

numlist = [10, 20, 12, 23, 58, 90]
s = 0
for v in numlist:
    s += v
avg = s/len(numlist)
print("Sum value is: ", s)
print("Avg value is:", avg)

print("Exampes of for loop")

mylist_1 = [1, 3, 9, 16, 25, 63, 81, 100]

for i in mylist_1:
    print(i*i)

num = int(input("Enter the number"))
for j in range(1, 11):
    print(num, "*", j, "=", num*j)

print("___________________________________-")


n = 5
for k in range(5):
    for x in range(k+1):
        print("*", end=" ")
    print(" ")

print("Pyramids")

size = 5
m = (2*size)-2
for y in range(0, size):
    for z in range(y, m):
        print(end=" ")
    m = m-1
    for z in range(0, y+1):
        print("* ", end=" ")
    print(" ")

print("Ascii values of alphabets")
print(ord("J"))

for let in range(65, 75):
    for nme in range(65, let+1):
        print(chr(nme), "=", nme, end=" ")
    print(" ")

captial_city = [["Chennai", "Bangalore", "Hyderabad"], [80, 90, 88]]

for item in captial_city:
    for item1 in item:
        print(item1)

print("Matrix")

n = int(input("Enter identity matrix value"))
for a in range(n):
    for b in range(n):
        if a == b:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print(" ")

fruits = ["Rasengan", "Chidori", "Sharingan", "Mangekoyu", "Shuriken"]

for val in fruits:
    print("Item is", val)
    for val2 in val:
        print(val2)

num1 = 15
for v in range(num1+1):
    for w in range(v):
        print(v, end=" ")
    print()

for nom in range(0, 1000, 12):
    if len(str(nom)) == 3:
        print(nom)
        break

val_list = [10, 20, 3, 7, 26]

for odd in val_list:
    if odd % 2 == 0:
        continue
    else:
        print(odd)
