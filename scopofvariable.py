str1 = "Python for Datascience"


def func():
    print(str1)


func()
print("-------------------------------------------------")
X = 8


def sum():
    X = 5
    y = 10
    return X+y


print(sum())
print(X)

print("++++++++++++++++++++++++++++++++++++++++++++++++")

x = 10


def f():
    global x
    x += 10
    print(x)


f()

print("value of x is", x)

print("---------------------------------------------------")


def sum_n():
    a = 10
    b = 20
    return a+b


print(sum_n())

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


def value():
    str1 = "Nezuko kamado"
    print(str1)


value()
