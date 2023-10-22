# Logical Operators --> used to find the logical relationship b/w the Operands
# There are mainly 3 types of Logical operands are there
# 1 And : Return true if both operands are true
# 2 or : Return false if at least one operand is false
# 3 not : Return the Opposite of the given Operand

# And Operators Example
# 1 Example using Boolean
a = True
b = False
result = a and b
print("And Operator :" , result)

# 2 Example using Expressions
x = 19
y = 123
result = (x>0) and (x<100)
print("And Operator: ", result)


# Or Operators Example
# 1 Example using Boolean
a = True
b = False
result = a or b
print("Or Operator: ", result)

# 2 Example using Expressions
x = 19
y = 123
result = (x>0) or (x<100)
print("Or Operator: ", result)

# And Operators Example
# 1 Example using Boolean
a = True
b = False
result = a and b
print(result)

# 2 Example using Expressions
x = 19
y = 123
result = (x>0) or (x<100)
print("Or Operator: ", result)

# not Operators Example
# 1 Example using Boolean
a = True
result = not a
print("Not Operator:",result)
# 2 Example using Expressions
x = 19
y = 123
result = not (x<100)
print("not Operator: ", result)

# 3 Example using Expressions with more Complex ones
x = 19
y = 123
result = (x>0) or (x<100) and (x==100)
print(" Operator: ", result)

# Practice Examples

# 1 Using and Operator both True conditions
a = 10
b = 5
c = "apple"
d = "apple"

result = (a>b) and (c==d)
print("1 : ",result)

# 2 Using and Operator one false condition
a = 10
b = 5
c = "apple"
d = "apples"
result = (a<b) and (c!=d)
print("2 : ",result)

# 3 Example Using and operator with one true and one false condtion
result = (5>=3) and (10!=10)
print("3 : ",result)

# 4 Using or Operator with 2 true conditions
res = ("car"=="car") or (7<9)
print("4 : ",res)

# 5 Using or Operator with 1 False condition
rest = ("dog"=="cat") or (6<10)
print("5 : ",rest)

# 6 Using or Operator with 2 False conditions
rests = (2==3) or (8>15)
print("6 : ",rests)

# 7 Using not Operator with 1 true condition
restss = not(4<=3)
print("7 : ",restss)

# 8 Using not Operator with 2 False conditions
rem = not("orange"=="orange")
print("8 : ",rem)

# 9 Using not Operator with and or
re = not((5>3) and ("apple" != "banana"))
print("9 : ",re)

# 10 Using and & not Operators combined
ret = (10>5) and not(3<2)
print("10 : ",ret)

# 11 Using or & not Operators combined
rety = ("cat"=="cat") or not(6<10)
print("11 : ",rety)

# 12 Using parentheses for group the expressions
reva = ((5>=3) and (10!=10) or (8>15))
print("12 : ",reva)

# 13 Using multiple and Operators
inp = (2<5) and (10==10) and ("hello" != "World")
print("13 : ",inp)

# 14 Using multiple or Operators
inps = (7<3) or (5>=5) or ("apple" == "apple")
print("14 : ",inps)

# 15 Using not Operator with an Expression
inpss = not(10>5 and "car" != "car")
print("15 : ",inpss)

# 16 Using not Operator with or & and
sem = not(5>3 or "dog" == "cat" and 7<5)
print("16 : ",sem)

# 17 Using Combining of and & or Operators
cons = (5>3 and "apple" != "banana") or (8==8 or 6<10)
print("17 : ",cons)

# 18 Combine the or & not Operators
sems = ("apple" =="banana" or not (6>10))
print("18 : ",sems)

# 19 Complex combination of and or not operators
hyd = not(2<5) and (7>3 or "hello"=="world")
print("19 : ", hyd)

# 20 Nested use of and or & not Operators
der = (not(5>3)and (10!=10 or "car"=="car"))
print("20 :", der)


