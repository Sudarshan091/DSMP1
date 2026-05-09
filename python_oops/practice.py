#problem 1.  creat a car class with attributes like brand and model
#then create an instances of this class 
# class car:
#     def __init__(self, brand,model,colour,price):
#         self.brand=brand
#         self.model=model 
#         self.colour=colour
#         self.price=price

# my_car=car("Toyota","corolla","red",200000)
# print(my_car.brand,my_car.model,my_car.colour,my_car.price)
# print(my_car.model)
# print(my_car.colour)
# print(my_car.price)

# my_new_car= car("tata","safari","pink",100000)
# print(my_new_car.brand,my_new_car.model,my_new_car.colour,my_new_car.price)
# print(my_new_car.model)
# print(my_new_car.colour)
# print(my_new_car.price)

# problem 2. add a method tp the car class that display the full name pf the
# car(brand , model , colour and price)

# class car:
#     def __init__(self,brand,model,colour,price):
#         self.brand=brand
#         self.model=model
#         self.colour=colour
#         self.price=price
#     def full_name(self):
#         return f"{self.brand},{self.model},{self.colour},{self.price}"

# class ElectricCar(car):
#     def __init__(self, brand,model,colour,price,battery_size):
#         super().__init__(brand,model,colour,price)
#         self.battery_size=battery_size

# my_electric_car=ElectricCar("Tesla","Model S","black",500000,100)
# print(my_electric_car.full_name())
# print(my_electric_car.battery_size) 


# my_car=car("Toyota","corolla","red",200000)
# print(my_car.full_name())
# my_new_car=car("tata","safari","pink",100000)
# print(my_new_car.full_name())

# problem 3. create an electric car class taht inherits from the car class and has an additional attribute battery_size

class car:
    def __init__(self,brand,model,colour,price):
        self.brand=brand
        self.model=model
        self.colour=colour
        self.price=price 
    def full_name(self):
        return f"{self.brand},{self.model},{self.colour},{self.price}"

class ElectricCar(car):
    def __init__(self,brand,model,colour,price,battery_size):
        super().__init__(brand,model,colour,price)
        self.battery_size=battery_size
    
        
my_electric_car=ElectricCar("Tesla","Model S","black",500000,100)
print(my_electric_car.full_name())
print(my_electric_car.battery_size)


#problem 4. modify the car class to encapsulate the brand attributes making it
#  private and provide a getter method for it 
 
        