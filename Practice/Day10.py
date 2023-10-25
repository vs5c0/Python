# Nested Conditional Stmts are used when the Conditions are in Complex
# 1 Example
x = 1

if x > 0:
    print("Its a Positive")
    if x%2==0:
        print("Its is a Even")
    else:
        print("X is a Odd")
else:
    print("x is not a positive")

# 2 Example

score = 60
if score >= 90:
    print("Grade A")
elif score >= 85:
    print("Good Job")
if score >= 80:
    print("Grade B")
elif score >=70:
    print("Grade C")
else:
    print("Fail")


# 1 Example Check given num is positive or negative or zero
num = 8
if num > 0:
    print("Positive")
elif num == 0:
    print("It is a Zero")
else:
    print("Negative")

# 2 Example Check given num is positive or negative or even or odd
x = -5

if x % 2 == 0:
    print("Its is a Even")
else:
    print("X is a Odd")
if x > 0:
        print("Its a Positive")
else:
    print("x is Negative")

# 3 Example find age of the list

age = 16
if age == 16:
    print("Teenager")
elif age == 2:
    print("Baby")
elif age >= 18:
    print("Adult")
else:
    print("child")

# 4 Example Grades
percentage = 61
if percentage >=90:
    print("Grade : A")
elif percentage >=80:
    print("Grade : B")
elif percentage >= 70:
    print("Grade: C")
else:
    print("Fail")

# 5 Example Leap Year
import calendar
year = 2024
month = 2
if (year % 4 == 0 and year % 100!= 0 or year%4 == 0):
   print("It is a Leap Year")
else:
    print("its is not a leap year")
    if month == 2:
         print("It is Feb")
         print(29)
    else:
        print(30)


