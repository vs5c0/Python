# Nested if Stmt --> a if Statement having another if statement then it is nested if

is_Male = True
is_Tall = True

if is_Male:
    if is_Tall:
        print("Your are a Tall")
        print("Your are a Male")
    else:
        print("Your are not a Male")