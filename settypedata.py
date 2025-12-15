set1 = {10,20,30,40,50}
print(set1)
print(type(set1)) 
set2 = {1,2,34,"css","html",45.67,1,2}
print(set2)
#built-in functions
print("Length of set2 is:", len(set2))
set2.add("javascript") #add
print("Set after adding one item using add():", set2)
set2.update(["react","angular","vue"]) #update
print("Set after adding multiple items using update():", set2)
set2.remove("html") #remove
print("Set after removing specific item using remove():", set2)
set2.discard("css") #discard
print("Set after discarding specific item using discard():", set2)
popped_item = set2.pop() #pop
print("Popped item is:", popped_item)
print("Set after popping an item using pop():", set2)
print("After using all built-in fun",len(set2))
set3 = {100,200,300,900}
set4 = {400,500,600,700,800}
#union
set_union = set3.union(set4)
print("Union of set3 and set4 is:", set_union)
#intersection
set_intersection = set3.intersection(set4)
print("Intersection of set3 and set4 is:", set_intersection)   
print("Disjoint sets?", set3.isdisjoint(set4))
print("Subset?", set3.issubset(set4)) 
print("SET DIFFERENCE:", set3.difference(set4))
