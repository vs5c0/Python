class s:
    def __init__(self,name,age,rate):
        self.name = name
        self.age = age
        self.rate = rate

    def on_the_honor(self):
        if rate >= 3.5:
            print("Eligible for honor")
        else:
           print("Not eligible for honor")