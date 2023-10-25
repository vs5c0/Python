# While Loop --> used to execute a block of code or repeat the code until the loop condition is satified when loop is false it became terminated
num = 1
while num <= 5:
    print(num)
    num = num + 1

# Example 2 sum of number using while loop

num = 1
sum = 0
while num <=10:
    sum += num
    num += 1
    print("Sum of Numbers:  ", sum)

# Example 1 prints number form 1 to 10
numb = 0
while numb <= 9:
    numb = numb +1
    print( "Prints numbers from 1 - 10 :", numb)

# Example 2 print sum of numbers using while loop
numw = 1
sums = 0
while numw<=5:
    sums = sums + numw
    numw = numw + 1
    print("sum of five numbers",sums)

# Example 3 print even number
numy = 2
while numy <= 10:
    print(numy)
    numy=numy+2

# Example 5  print a numbers down from 10 to 1
your = 10
while your > 0:
    print(your)
    your= your-1

# 6 Example Ask user to find secret number

i = int(input("Enter Number: "))
while i == 7:
    print("Your Enter correct number")
    i = i+1

# Example 7  Factorial of a Number
def factorial(n):
    nusm = 1
    while n >= 1:
        nusm = nusm * n
        n = n - 1
    return nusm
f = factorial(10)
print("Factoral of Number :" ,f)

# Example 8 Fibbonbi series problems
n = int(input("Enter a Num: "))
a = 0
b = 1
sume = a + b
count = 1
print("Fibonacci series is: ", end=" ")
while (count <= n):
    count += 1
    print(a, end=" ")
    a = b
    b = sume
    sume = a + b

# example 9

yur = 1
sumss = 0
while yur <= 10:
    sumss=sumss+yur
    yur=yur+1
    print("Sum of the Number",sumss)
# example 10 print the square of a number

    number = 1
    while number <= 5:
        print(number, "squared is", number ** 2)
        number += 1
    print("Square of a Number",number)

#example 4 print the neg number

hu = int(input("Enter a Number: "))
while hu < 0:
    print("it is a Neg Number")
    hu = int(input("Enter an Number :" ))
    while hu > 0:
        print("It is a not Neg number")
