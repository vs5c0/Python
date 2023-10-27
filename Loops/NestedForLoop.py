# Nested for loop --> is type of for loop , a for loop having another for loop

# Example program
nun = [
    [1,4,3,5],
    [5,7,8,4],
    [3]
]

for row in nun:
    for col in row:
        print(col)
        