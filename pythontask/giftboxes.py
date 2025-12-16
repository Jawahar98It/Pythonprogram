def guessfunc(a,b,c):
    for i in range(1,201):
        if (i%5 ==a) and (i%6 ==b) and (i%7 ==c):
            return i

num1 = int(input("Enter remainder when divided by 5: "))
num2 = int(input("Enter remainder when divided by 6: "))
num3 = int(input("Enter remainder when divided by 7: "))

print("The guessed number is:", guessfunc(num1,num2,num3))