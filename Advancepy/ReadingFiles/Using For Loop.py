# By using for loop we can read the files based on the conditions
# we can use the readLines() can display all text in file

EE_files = open("Emp.text", "r")
for emp in EE_files.readlines():
    print(emp)
    EE_files.close()