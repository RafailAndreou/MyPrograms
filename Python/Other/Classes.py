class person:
    Amount = 1.04
    def __init__(self,First_Name,Second_Name,Pay):
        self.First_Name = First_Name
        self.Second_Name = Second_Name
        self.Pay = Pay

    def Increase(self):
        self.Pay = int(self.Pay  * self.Amount)

John = person("John","Michael", 5000)
Will = person("Will","Smith",100000)
