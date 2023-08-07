print("Absolute value", abs(-99.34))
l1 = [44, -45, -56, 34, 90, -34, 12, 34, -10, -90, 20, 30]
print("Length of the list is", len(l1))
print("Sum of the list is", sum(l1))

str1 = "AttackonTitans"
print("Length of the string", len(str1))

fruits = "apple,kiwi,grapes,guava,banana"
fruits = fruits.split(',')
print(fruits)
print(len(fruits))

print("________________________________________________________")

print("Map function")

marks = [20, 23, 34, 44, 33, 10, 43, 23, 27, 34, 37, 44, 42, 43]
per_mrks = list(map(lambda x: round((x/45)*100, 2), marks))

print(per_mrks)
print("___________________________________________________")
# help(map)

list_a = [10, 20, 30]
list_b = [12, 5, 70]
add_num = list(map(lambda x, y: x+y, list_a, list_b))

print(add_num)

print("=====================================================")

print("Filter function")


def isodd(x):
    if x % 2 != 0:
        return x


print(isodd(15))


def cub(x):
    return x**3


print(cub(3))

odd_num = list(filter(isodd, range(1, 51)))
print(odd_num)
cube_val = list(map(cub, filter(isodd, range(1, 51))))
print(cube_val)
print(sum(list(map(cub, filter(isodd, range(1, 51))))))

letters = ["beach", "car"]
funified = list(map(lambda word: f"{word} is fun!", letters))
print(funified)
