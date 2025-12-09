str1 = "DemonSlayer"
l1 = []
for i in str1:
    l1.append(i)
print(l1)
print("----------------------------------------------")

num = [14, 22, 5, 34, 16]
[print(j**2) for j in num]

print("--------------------------------------------------------")
list_1 = ["python", "is", "finest", "programming", "language", "or","not?"]
print([(item.upper()) for item in list_1])

print("--------------------------------------------------------------")
cube_num = [2, 5, 6, 7, 8]
print([([cub**2, cub**3]) for cub in cube_num])

print("Nested loop list comprehension")

print([[num*num1 for num1 in range(1, 11)] for num in range(13, 18)])
print("--------------------------------------------------------------------------------------")
list_a = [20, 55, 25, 45, 78]
list_b = [12, 78, 69, 2, 55]
print([(val1, val2) for val1 in list_a for val2 in list_b if val1 < val2])

print("============================================================")

print("List comprehension using if condition")

even_num = [x for x in range(1, 11) if x % 2 == 0]
print(even_num)

print("-----------------------------------------")

print([y**2 if y % 2 == 0 else y**3 for y in range(1, 11)])

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")

num_1 = [1, 24, 36, 4, 54, 60, 72, 8, 9, 10]
print([divi for divi in num_1 if divi % 2 == 0 if divi % 3 == 0])

print("###############################################################")

print(["Even num:" if odeve % 2 == 0 else "Odd num:" for odeve in range(0, 20)])

print("***************************************************************")

comp_1 = [102, 232, 233, 344, 456, 564, 234]
comp_2 = [102, 233, 324, 567, 564, 523, 456]

print([v for v in comp_1 for v1 in comp_2 if v == v1])

print("Dictionary comprehension ")

print({z: z**2 for z in range(1, 11)})
