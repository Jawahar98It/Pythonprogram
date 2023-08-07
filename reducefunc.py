from functools import reduce
from itertools import accumulate
sales = [2345, 2344, 1234, 6789, 9876]
print(reduce(lambda x, y: x+y, sales))

print("Factorial value of 5 is", reduce(lambda x, y: x*y, range(1, 6)))
print("list of factorial 5 is", list(range(1, 6)))

print("Accumulate fun", list(accumulate(range(1, 7), lambda x, y: x+y)))

print("Reduce fun", reduce(lambda x, y: x+y, range(1, 7)))
