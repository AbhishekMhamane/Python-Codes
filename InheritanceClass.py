class vehical:
    def print(self):
        print("in the vehical class")
class car(vehical):
    def __init__(self,name):
        self.name = name
    
    def printCar(self):
        print("Car name : ",self.name)


c = car("ford")
c.print()
c.printCar()

        