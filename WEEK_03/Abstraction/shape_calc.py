"""The Challenge: "Shape Calculator"
Create an abstract base class called Shape with the following requirements:

Abstract Method: Define an abstract method called area().

Concrete Class: Create a class named Rectangle that inherits from Shape.

It should accept width and height in its constructor (__init__).

Implement the area() method to return the result of width * height.

Testing: Instantiate the Rectangle class with values of your choice 
(e.g., width 5, height 10) and print the result of the area() method."""


from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,width,height):
        self.w=width
        self.h=height
    def area(self):
        toatl_area=self.w*self.h
        return toatl_area
rect=Rectangle(5,10)
Height=rect.h
Width=rect.w
# print(f"rectangle height:{Height}\n          width:{Width}")
ar=rect.area()
# print(ar)
# Using \n for a new line and descriptive names
print(f"Rectangle Height: {rect.h}\nRectangle Width: {rect.w}")
print(f"The total area is: {ar}")