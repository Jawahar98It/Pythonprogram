set1 = set()
print(type(set1))
set1 = {'Python', 'HTML', 'CSS', 1, 2, 3}
print(set1)
set2 = {12, 12, 45, 34, 25, 56}
print(set2)
set2.add(90)
print(set2)
set2.update([20, 92])
print(set2)
print(len(set2))
set1.remove(2)
print(set1)
set2.pop()
print(set2)
set2.remove(92)
print(set2)
val1 = {1, 2, 3, 4}
val2 = {5, 6, 7, 8, 9}
print(val1.isdisjoint(val2))
data1 = {11, 12, 13, 14, 15}
data2 = {11, 12, 13, 14, 19, 16, 17}
print(data1.issubset(data2))
print("union vales \n", val1.union(val2))
print("Intersection values \n", data1.intersection(data2))
print("Difference value \n", data1.difference(data2))
