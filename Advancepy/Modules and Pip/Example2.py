import random
feet_in_mile = 5280
meters_in_Kilometers =1000
beatles = ["Ram","Kiran","Vikrams"]

def get_file_ext(filename):
    return filename[filename.index(".")+1:]

def roll_dice(num):
    return random.randint(1,num)