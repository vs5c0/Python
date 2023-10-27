# Exponent Function ---> used to solve the math problems
# Used to take a number and get the power of the number

# Example 1
print(8**3)
print(2**4)

# Example 2

def raise_to_power(Base_num, Pow_num):
    result = 1
    for index in range(Pow_num):
        result = result * Base_num
        return result
    print(raise_to_power(2,4))

#Output
 # 16