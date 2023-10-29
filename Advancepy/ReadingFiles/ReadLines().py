# readLines() are used to read all the text in the text files in an array format

E_files = open("Emp.text", "r")
print(E_files.readlines())
E_files.close()

# readLines() are used to read all the text in the text files in an array format by using [] index

E_files = open("Emp.text", "r")
print(E_files.readlines()[2])
E_files.close()