def average(x):
    s = 0
    for i in x:
       s += i
    avg = s / len(x)
    return avg
list1 = [10,20,30,40,50]
result = average(list1)
print("Average of the list is:", result) 

def greet(name):
    return f"Hello, {name}! Welcome to GreatLearning."

print(greet("Alice"))

def unique(unique_list):
    l1 = []
    for i in unique_list:
        if i not in l1:
            l1.append(i)
    return l1
unique_list = [1,2,2,3,4,4,5,5,6]
result = unique(unique_list)
print("Unique elements in the list are:", result)

#reversing string
def reverse_string(x):
    s = ''
    for i in x:
        s = i + s
    return s
x = "GreatLearning"
reversed_str = reverse_string(x)
print("Reversed string is:", reversed_str)

def reverse_data(data):
    rev_data = data[::-1]
    return rev_data
data = "Functional Data"
reversed_data = reverse_data(data)
print("Reversed data is:", reversed_data)

def multiplytable(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
number = int(input("Enter a number to print its multiplication table: "))
multiplytable(number)

l1 = [11,12,14,18,19]
def product_of_list(lst):
    product = 1
    for i in lst:
        product *= i
    return product
product_of_list_result = product_of_list(l1)
print("Product of all elements in the list is:", product_of_list_result)

def identity_matrix(x,y):
    for i in range(x):
        for j in range(y):
            if i == j:
                print(y, end="")
            else:
                print(0, end="")
        print()

identity_matrix(4,4)

def variable_args(*args):
    for arg in args:
        print(arg)

variable_args(1, "Hello", 3.14, [1, 2, 3])

def varfunc(*args):
    print(args)
varfunc(10, 20, 30, 40, 50)

def keyword_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
keyword_args(name="Alice", age=30, city="New York")

def sum_n(x):
    if len(x) == 0:
        return 0
    last_num =x.pop()
    return last_num + sum_n(x)
numbers = [1, 2, 3, 4, 5]
result = sum_n(numbers)
print("Sum of numbers using recursion is:", result)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i), end=" ")
