from functools import reduce
from itertools import accumulate
string = "Python for Data Science"
def function_example():
    print(string)
function_example()

#lambda function to add two numbers
min_value = lambda a,b: a if a < b else b
print("Minimum value is:", min_value(10, 20))

str_x = "Frappe"
str_y = "frappe"

compare_strings = lambda a,b: "True" if str_x == str_y else "False"
print("Are the two strings equal (case sensitive)?", compare_strings(str_x, str_y))

#builtin functions

marks = [55, 78, 90, 67, 88,33,45,55]
per_marks = map(lambda x: round(x/45*100,2), marks)
print("Percentage marks are:", list(per_marks))

#print(help(map))

list_a = [1,2,3,4,5,6,7,8,9]
list_b = [10,20,30,40,50,60,70,80,90]
mapped_list = map(lambda x,y: x+y, list_a, list_b)
print("Mapped list after adding corresponding elements:", list(mapped_list))

def isodd(x):
    if x % 2 !=0:
        return x
odd_numbers = filter(isodd, range(1,21))
print("Odd numbers between 1 and 20 are:", list(odd_numbers))

sales = [1000, 2000, 3000, 4000, 5000]
total_sales = reduce(lambda x,y: x+y, sales)
print("Total sales amount is:", total_sales)

fact_value = reduce(lambda x,y : x*y, range(1,6))
print("Factorial of 5 is:", fact_value)

accumulated_sum = list(accumulate(range(1,6), lambda x,y: x+y))
print("Accumulated sum of numbers from 1 to 5 is:", accumulated_sum)
