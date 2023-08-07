def recur(x):
    if len(x) == 0:
        return 0
    last_num = x.pop()
    return last_num+recur(x)


l1 = [10, 12, 5, 6, 8, 10]
sum_of_lst = recur(l1)
print(sum_of_lst)

print("___________________________________________________________")


def fibonacci(a):
    if a == 0:
        return 0
    if a == 1:
        return 1
    return fibonacci(a-1)+fibonacci(a-2)


for i in range(15):
    print(fibonacci(i), end=' ')
