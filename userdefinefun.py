def average(x):
    '''
    get average using function
    '''
    s = 0
    for i in x:
        s += i
    avg = s/len(x)
    return avg


l1 = input("Enter the number sequence seperated by commas")
l1 = [float(item) for item in l1.split(',')]
print(l1)
l1_avg = float(average(l1))
print(round(l1_avg))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def greet(name):
    print("Hello", name, "How are you?")


greet("Nezuko")

print("`````````````````````````````````````````````````````````````````````")


def common(num_list):
    num1 = []
    for x in num_list:
        if x not in num1:
            num1.append(x)
    return num1


num_list = [44, 45, 56, 44, 32, 54, 44, 56, 44, 87, 44, 56]

unique_list = common(num_list)
print(unique_list)

print("*****************************************************************************")


def reverse(str1):
    s = ''
    for j in str1:
        s = j+s
    return s


print(reverse("Nezuko"))

print("___________________________________________________________________________________")


def multiplication(table):
    for num in range(1, 11):
        print(table, "*", num, "=", table*num)


multiplication(5)

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

l2 = [12, 14, 16, 18, 4, 5]


def product(l2):
    p = 1
    for a in l2:
        p = p*a
    return p


print(product(l2))


def identity(m1, m2):
    for i in range(m1):
        for j in range(m2):
            if i == j:
                print(m2, end=" ")
            else:
                print(0, end=" ")
        print()


identity(3, 3)

print("-------------------------------------------------")

print(min(10, 12, 14, 14, 9, 23))


def varfun(*args):
    print(args)


varfun(10, 2, 34, 1, 0.3)

print("----------------------------------------------------------")


def varfun1(*a):
    for i in a:
        print(i)


varfun1(10, 23, 4, 9, 24)

print("===============================================================")


def kvarfunc(**kvargs):
    print(kvargs)


kvarfunc(a=22, b=33, c=11, d=10, e=9)

print("-----------------------------------------------------------------")


def kwarfunc(**kwargs):
    for i, j in kwargs.items():
        print("Key is", i)
        print("value is", j)


kwarfunc(x='Nezuko', y='Inosuke', z='Zenistu', A='Tanjiro')
