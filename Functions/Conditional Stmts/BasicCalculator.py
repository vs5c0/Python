# Build a basic calculator

num1 = float(input("Enter first Number : "))
operator = input("Enter a Operator : ")
num2 = float(input("Enter Second Number : "))
if operator == "+":
    print("Sum of Two Number : ",num1+num2)
elif operator == "-":
    print("Sub of Two Number : ",num1-num2)
elif operator == "*":
    print("Multiply of Two Number : ",num1*num2)
elif operator == "/":
    print("Divison of Two Number : ",num1/num2)
else:
    print("Invaild Operator U entered ")