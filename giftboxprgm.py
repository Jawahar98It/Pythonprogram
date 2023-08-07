# Sample input & output
# if the gift is divided by 2 people, how many gifts would be leftover? -> ans is 2
# if the gift is divided evenly among 6 people, how many gifts would be leftover -> ans is 3
# if the gift is divided evenly among 7 people, how many gifts would be leftover -> ans is 2
# number of gifts in the jar: 177

def guess(a, b, c):
    for i in range(1, 200):
        if (i % 5 == a) and (i % 6 == b) and (i % 7 == c):
            return i


print("if the gift is divided among 5 people, how many gifts would be leftover?")
a = int(input())
print("if the gift is divided among 6 people, how many gifts would be leftover?")
b = int(input())
print("if the gift is divided among 7 people, how many gifts would be leftover?")
c = int(input())
gift = guess(a, b, c)
print("Number of gifts are", gift)
