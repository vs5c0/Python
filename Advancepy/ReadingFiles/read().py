# read() is used to display all the text in the text file

emps_files = open("Emp.text", "r")
print(emps_files.read())
emps_files.close()