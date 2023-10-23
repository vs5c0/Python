# if Stmt Example
age = 18
if age >= 18:
    print("Your are an Eligible")
# if Else Stmt Example
age = 15
if age>= 18:
    print("Your are a Adult")
else:
    print("your are a Minor")

# Example Elif Stmts
age = 25
if age < 18:
    print("Your are a Minor")
elif age>= 18 and age < 65:
    print("Your are an Adult")
else:
    print("Your are a Senior Citizen")

# Example 1 Given number is Even or Odd

num = 7
if num%2==0:
    print("It is an Even")
else:
    print("It is an Odd")

# Example 2 Take input from user and print Largest number

nums = input("Enter the 1 st number: ")
nums2 = input("Enter the 2 nd number: ")
if (nums > nums2):
    print(nums)
elif (nums2 < num):
    print(nums2)

else:
    print("both are equal")

# Example 3 Take input from user and display output as vowels

chars = input("Enter a Character :")
if(chars == "a" or chars=="e"or chars =="i"or  chars =="o"or chars =="u"):
 print("It is a Vowel")
else:
    print("It is a Constants")

# Example 4 program a year is a leap year are not
year = int( input("Enter the Year :"))

if (year%4 ==0 and year%100!=0 or year%4==0):
    print("It is a Leap Year")
else:
    print("its is not a leap year")

# Example 5 Grades program

grades = input("Enter a grade : ")
if (grades == "A" or grades == "B" or grades == "C" or grades =="D"):
    print("Pass")
else:
   print("Fail")