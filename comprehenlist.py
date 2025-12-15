#comprehension list
str1 = "GreatLearning"
result = [i for i in str1]       
print("List using comprehension:", result)
data = [10,12,15,24]
squared = [x**2 for x in data]
print("Squared values using comprehension:", squared)
list1 = ["what","happening","to","you","today?"]
upper_list = [word.upper() for word in list1]
print("Uppercase words using comprehension:", upper_list)
newlist = [11,12,15,17]
newlist_result = [[v**2,v**3] for v in newlist]
print("List of squares and cubes using comprehension:", newlist_result)

#comprehesion nested loops
new_data = [[v*j for j in range(1,11)]for v in range(12,17)]
print("Nested comprehension list:", new_data)

list_1 = [12,13,72,27,45,60]
list_2 = [24,78,12]
tup_convert = [(v1,v2) for v1 in list_1 for v2 in list_2 if v1 < v2 ]
print("List of tuples using nested comprehension:", tup_convert)
#conditional comprehension
eve_list = [i**2 if i%2 == 0 else i**3 for i in range(1,11) ]
print("Even numbers using comprehension:", eve_list)
dict_value = {i:i**2 for i in range(1,11)}
print("Dictionary using comprehension:", dict_value)