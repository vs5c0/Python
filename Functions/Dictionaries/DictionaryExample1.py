# Dictionaries --> Dictionary in python is used to store the different type of data
# --> Dictionary store the data in the key value pair
# Dictionary is seperated by comma(,) and { } values are store in the Sqaure Brackets

Week = {
    1 : "Monday",
    2 : "Tuesday",
    3 : "Wednesday",
    4 : "Thursday",
    5 : "Friday",
    6 : "Saturday",
    7 : "Sunday",
}
print(Week[1])
print(Week.get(3))
print(Week.get(9, "not present in Dictionary"))