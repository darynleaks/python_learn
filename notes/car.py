#description class for descripe imagine car
class Car():
    #add variable for class
    wheels = 4
    #add method
    def drive (self):
        print("Driving so fast")
#create instance for car
my_car = Car

#Calling atribute of class
print (my_car.wheels)

#calling method
my_car.drive(self='some words')