mylist = ["Java", "Python", "Machine Learning"]
str1 = "Python"
if str1 in mylist:
    print(str1, "tutorial")
print("-----------------------------------------------------")
str2 = "c"
if str2 in mylist:
    print(str2, "tutorial")
else:
    print(str2, "is not present in list")
print("-----------------------------------------------------")
if "Java" in mylist:
    print(True)
x = 200
if not x == 500:
    print(x, "is not equal to 500")
else:
    print(x, "is equals to 500")
print("------------------------------------------")
y = 500
if y == 500:
    print(y, "is equal to 500")
else:
    print(y, "is not equals to 500")
print("-----------------------------------------------------")
n = 150
result = n*8 if n > 400 else n/8
print(result)
print("-----------------------------------------------------")
n1 = 450
result1 = n1*8 if n1 > 400 else n1/8
print(result1)
print("-----------------------------------------------------")
usrname = input("Enter username:")
pswrd = input("Enter password:")
if usrname == "Bujilikutty" and pswrd == "Thenu@0111":
    print("Successfully logged in")
else:
    print("Invalid credentials")
print("-----------------------------------------------------")
var = 1+5j

if (type(var) == int):
    print(var, "is integer")
elif (type(var) == float):
    print(var, " is float")
elif (type(var) == str):
    print(var, " is string")
elif (type(var) == bool):
    print(var, " is bool")
elif (type(var) == complex):
    print(var, " is complex")
elif (type(var) == list):
    print(var, " is list")
else:
    print("Nothing")
print("-----------------------------------------------------")
num = 10
if num == 0:
    print(num, " is equal to zero")
elif num > 50:
    print(num, " is greater than 50")
elif num < 50:
    print(num, " is less than 50")
else:
    print("Not a number")

print("-----------------------------------------------------")
num1 = float(input("Enter the number"))
if num1 >= 0:
    if num1 == 0:
        print(num1, "Number is equal to zero")
    else:
        print(num1, "Number is positive")
else:
    print(num1, " is negative")

print("-------------------------------------------------")
score = float(input("Enter the marks"))
if (score <= 100 and score >= 90):
    print("Distinction")
elif (score < 90 and score >= 80):
    print("First Class")
elif (score < 80 and score >= 70):
    print("Second Class")
elif (score < 70 and score >= 60):
    print("Third Class")
elif (score < 60 and score >= 50):
    print("Fourth Class")
elif (score == 50):
    print("Fifth Class")
elif (score < 50 and score >= 0):
    print("Just Pass")
else:
    print("Enter valid score between 1 nd 100")
