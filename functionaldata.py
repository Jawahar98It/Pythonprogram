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