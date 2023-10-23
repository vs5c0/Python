# "And Operator " --> if a both stmts are true then it returns true otherwise false

result = (10>5) and (10==10)
print("And Operator:",result)

# "or Operator " --> if at least one stmt are true then it returns true otherwise false

result1 = (10>5) or (10==10)
print("Or Operator:",result1)

# "not Operator " --> Opposite of the give condition

result2 = not(10==10)
print("Not Operator:",result2)

# Example program using and or not Operators
is_Male = True
is_Tall = False
if is_Male and is_Tall:
    print("Your are a Male and Tall")
elif is_Male and not(is_Tall):
    print("Your are a Male but not a Tall")
elif not(is_Male) and is_Tall:
    print("Your are not a Male but Your are tall")
else:
    print("Your are a Female")