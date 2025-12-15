mylist = []
print(type(mylist))
mylist1 = list()
print(type(mylist1))
mylist2 = [["DS","ML","AI"],[100,90,80]]
print(mylist2)
#indexing
course_list = ["DS","ML","AI","Python","JavaScript"]
print(course_list[1])
print(course_list[-1])
print(course_list[3])
print(course_list[-3])
#length of list
print("Length of course_list is:", len(course_list))
print("Length of mylist2 is:", len(mylist2))
#slicing
print("Retrive elements from index 1 to 3:", course_list[0:3])
print("Retrive last 3 elements:", course_list[-3:])
print("Without specifying start and stop index:", course_list[:])
print("Retrive elements from index 0 to 4:", course_list[0:4])
print(course_list[0:5:2])
print(course_list)

#modifying list
course_list[0] = "Data Science"
print("After modifying list:", course_list)

#builit-in functions
course_list.append("HTML") #append
print("Add one item in list using append():",course_list)
course_list.insert(2,"CSS") #insert
print("Add one item at specific index using insert():",course_list)
course_list.extend(["C++","Java"]) #extend
print("Add multiple items using extend():",course_list)
course_list.sort() #sort
print("Sort the list using sort():",course_list)
course_list.sort(reverse=True) #sort in descending order
print("Sort the list in descending order using sort():",course_list)
course_list.sort(key=len) #sort by length of string
print("Sort the list by length of string using sort():",course_list)
del course_list[3] #delete using del
print("Delete item at specific index using del:",course_list)
del course_list[4:6] #delete multiple items using del
print("Delete multiple items using del:",course_list)
mylist2.clear() #clear
print("Clear all items using clear():",mylist2)
course_list.remove("Java") #remove
print("Remove specific item using remove():",course_list)
course_list.pop() #pop
print("Remove last item using pop():",course_list)
course_list.reverse()
print("Reverse the list using reverse():",course_list)

new_course = ["Frappe","Django","Flask"]
new_course2 = ["React","Angular","Vue"]
all_courses = course_list + new_course + new_course2
print("Concatenate multiple lists:", all_courses)

print("repetoition of list:", new_course * 3)