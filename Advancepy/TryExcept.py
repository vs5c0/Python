# Try Except --> used to solve the errors in python

try:
    value = 10/10
    num = (int(input("Enter a number : ")))
    print(num)
except ZeroDivisionError as err:
    print(err)
except ValueError as vala:
    print(vala)