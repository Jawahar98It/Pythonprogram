a = 0
while a < 5:
    print(a)
    a += 1
print("--------------------------------------------------------")
sum = 0
a1 = 0
while a1 <= 10:
    sum += a1
    a1 += 1
print(sum)
print("----------------------------------------------------------")
n = 7
while n > 0:
    n -= 1
    if n == 2:
        continue
    else:
        print(n)

print("======================================================================")
n1 = 7
while n1 > 0:
    n1 -= 1
    if n1 == 2:
        break
    else:
        print(n1)

print("-------------------------------------------------------------")

wrd = input("Enter message")
while True:
    if wrd == "Hello":
        break
    else:
        wrd = input("Enter second message:")
print("---------------------------------------------------------")
sum_n = 0
count_n = 0
while True:
    count_n += 1
    if count_n > 4:
        break
    sum_n = sum_n+count_n
print("sum of first four numbers:", sum_n)

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")

n2 = 10
while n2 > 0:
    n2 -= 1
    if n2 == 4:
        continue
    print(n2)
