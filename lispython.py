my_list = []
print(type(my_list))
name_list = list()
print(type(name_list))
my_list = [['Ds', 'ML', 'Py'], [100, 200, 300]]
print(my_list)
my_list[1][0] = 23
print(my_list)
name_list = ["Power BI", "Data Science", "Machine Learning", "Python", "HTML"]
print(name_list[1])
print("Negative indexing :\n", name_list[-2])
print("Negative index of mylist", my_list[-1])
print("Length of list", len(my_list))
print("Length", len(name_list))
print("Slicing list", name_list[0:3])
print("Slicing list using negative index", name_list[-3:])
print(my_list[1:])
print(name_list)
name_list[2] = 'ML'
print(name_list)
name_list.append("Automation")
print(name_list)
my_list.insert(1, "DCT")
print(my_list)
name_list.extend(["Java", "Selenium"])
print(name_list)
name_list.sort()
print("Sorting list", name_list)
name_list.sort(reverse=False)
print("sorting methods \n", name_list)
name_list.sort(reverse=True)
print(name_list)
name_list.sort(key=len)
print(name_list)
print("Deleting list")
del name_list[2]
print(name_list)
print("Delete list using slice methods")
del name_list[2:5]
print(name_list)
age = [18, 19, 20, 21, 22]
age.clear()
print(age)
print("Remove methods inlist")
name_list.remove('Automation')
print(name_list)
print("pop methods in list")
my_list.pop()
print(my_list)
print(name_list)
print("Reversing list data")
name_list.reverse()
print(name_list)
print("Concatenation methods")
courses = ['ML', 'AI']
course1 = ['SQL', 'BI']
print(courses+course1)
print("Repetiton methods")
print(course1*3)
