tup1 = ("Python","ML","DS","AI")
print(type(tup1))
print(tup1)
tup2 = (100,200,300,400)
print(tup2)
tup3 = ("Python",["ML","DS"])
print(tup3)
tup4 = ((1,2,3),(4,5,6))
print(tup4)

#indexing
color_tup = ("Red","Green","Blue","White","Black","Yellow","Orange","Purple","Red","Purple")
print(color_tup[1])
print(color_tup[-2])
#slicing
print(color_tup[3:5])
print(color_tup[-3:-1])
#changing values of tuple
#tuples are immutable, so we cannot change the values of tuple
#but we can change if list is present inside the tuple
tup5 = (10,20,["Python","ML","DS"],40)
print("Before changing value inside list in tuple:", tup5)
tup5[2][1] = "AI"
print("After changing value inside list in tuple:", tup5)
#del tup5
#print("Tuple deleted",tup5)

#count methods
print(color_tup.count("Red"))
print(color_tup.count("Purple"))