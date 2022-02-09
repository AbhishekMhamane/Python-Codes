class Car:
    def printcarName(self,name):
        print("Car Name :",name)
        
class Bike:
    def printbikeName(sel,name ):
        print("Bike Name :",name)

class Owner(Car,Bike):
    def printownerName(self,ownerName,name2,name3):
        print("Owner Name :",ownerName)
        Car.printcarName(self,name2)
        Bike.printbikeName(self,name3)


obj = Owner()
obj.printownerName("Abhishek","BMW","RE")