mylist = ["Data Science", "Machine Learning", "Artificial Intelligence","Python","JavaScript"]
course = "C"
if course in mylist:
    print(f"{course} is present in the list")
else:
    print(f"{course} is not present in the list")
if "Python" in mylist:
    print("Python is present in the list")
else:
    print("Python is not present in the list")
x = 500
if not x == 500:
    print("x is not equal to 500")
else:
    print("x is equal to 500")
n = 150
result = n*8 if n > 100 else n/8
print("Result is:", result)
a = 10
b = 20
if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")
    
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "admin123":
    print("Login successful")
else:
    print("Login failed")

var = 1 + 3j
if (type(var) is int):
    print(f"Variable {var} is of integer type")
elif (type(var) is float):
    print(f"Variable {var} is of float type")
elif (type(var) is complex):
    print(f"Variable {var} is of complex type")
elif (type(var) is str):
    print(f"Variable {var} is of string type")
elif (type(var) is list):
    print(f"Variable {var} is of list type")
elif (type(var) is tuple):
    print(f"Variable {var} is of tuple type")
elif (type(var) is set):
    print(f"Variable {var} is of set type")
elif (type(var) is dict):
    print(f"Variable {var} is of dictionary type")
elif (type(var) is bool):
    print(f"Variable {var} is of boolean type")
else:
    print("Unknown data type")
x = 15
if x ==0:
    print("x is zero")
elif x > 50:
    print("x is greater than 50")
else:
    print("x is not greater than 50")

number = float(input("Enter your number: "))
if number >= 0:
    if number == 0:
        print("You entered zero")
    else:
        print("You entered a positive number")
else:
    print("You entered a negative number")

score = int(input("Enter your score: "))
if (score <=100 and score >=90):
    print("Distinction")
elif (score <90 and score >=75):
    print("First Class")
elif (score <75 and score >=60):
    print("Second Class")
elif (score <60 and score >=40):
    print("Pass Class")
else:
    print("Fail")

