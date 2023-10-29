# Reading the files in python is used to read the files
# Mainly used to read the files by using the readable(), read(), readLines(), readLine()
# open & close plays a key role in reading a files
# readable() --> used to display the True or False as a results
emp_files = open("Emp.text", "r")
print(emp_files.readable())
emp_files.close()