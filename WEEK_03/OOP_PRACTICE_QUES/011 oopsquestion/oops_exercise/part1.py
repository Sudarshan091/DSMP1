#       ****** THESE QUESTION ARE FROM GEMINI ******

"""Your Goal: Create a simple blueprint and bring it to life.

Create a class called Dog.

Give it an __init__ constructor that accepts two parameters: name and breed. Assign these to the object.

Write an instance method called bark() that prints a message like: "Woof! My name is [name] and I am a [breed]."

The Test: Create two different dog objects (e.g., a Golden Retriever named "Buddy" and a Poodle named "Lucy") and call the bark() method on both of them."""

# class Dog:
#     def __init__(self,name,breed):
#         self.name= name
#         self.breed= breed
#     def bark(self):
#         print(f"Woof! My name is {self.name} and I am a {self.breed}.")

# dog1=Dog("Buddy","Golden Retriever")
# dog2=Dog("Lucy","Poodle")

# dog1.bark()
# dog2.bark()

"""Level 2: Doing the Math (Instance Variables and Logic)
Your Goal: Use a class to store data and perform calculations on that specific data.

Create a class called Rectangle.

Give it an __init__ constructor that accepts length and width.

Write a method called calculate_area() that returns the area of the rectangle (length * width).

Write a method called calculate_perimeter() that returns the perimeter (2 * length + 2 * width).

The Test: Create a Rectangle object with a length of 5 and a width of 10. Print out both its area and its perimeter."""

# class Rectangle:
#     def __init__(self,l,w):
#         self.l=l
#         self.w=w
#     def Calculate_area(self):
#         area=self.l*self.w
#         print(f"area of rectangle = {area}")

#     def calculate_perimeter(self):
#         peri=2*(self.l+self.w)
#         print(f"perimter of rectangle = {peri}")
# rect1=Rectangle(2,8)
# rect2=Rectangle(87,90)
# rect1.Calculate_area()
# rect1.calculate_perimeter()
# rect2.Calculate_area()
# rect2.calculate_perimeter()


"""Level 3: Guarding the Data (Basic Encapsulation)
Your Goal: Protect your data by making an attribute private and using methods to interact with it safely.

Create a class called Student.

Give it an __init__ constructor that accepts a name.

Inside the constructor, also create a private attribute called __grades and set it to an empty list []. (Remember, the user shouldn't pass this in; it just starts empty).

Write a method called add_grade(grade). This method should append the new grade to the private __grades list, but only if the grade is between 0 and 100. If it's invalid, print an error message.

Write a method called get_average() that calculates and returns the average of the student's grades.

The Test: Create a student named "Alex". Add the grades 85, 90, and 105 (this one should fail!). Then print Alex's average."""


# class Student:
#     def __init__(self,name,grade):
#         self.name=name
#         self.__grade=grade
#         grade=[]
#     def add_grade(self,grade):
#         grade=[85,90,105]



#         if 0<= grade <=100:
#             total=sum(grade)
#             self.__grade+=total
#         else:
#             print("invalid marks try with differnt marks")   
#     def get_average(self):
#         return total/len(grade)
        
# obj=Student("ALEX",[85,90,105])
# st1=obj.add_grade()
# st1=obj.get_average()
# st2=obj.add_grade()
# st2=obj.get_average()

# class Student:
#     # 1. We only need the name to create the student
#     def __init__(self, name):
#         self.name = name
#         # 2. The private grades list starts completely empty automatically
#         self.__grades = [] 

#     # 3. Add 'self' as the first parameter, and take ONE grade at a time
#     def add_grade(self, grade):
#         # Check if the single grade is valid
#         if 0 <= grade <= 100:
#             # Append it to the private list!
#             self.__grades.append(grade)
#             print(f"Added {grade} to {self.name}'s file.")
#         else:
#             print(f"Error: {grade} is an invalid mark. Try a different mark.")   

#     # 4. Don't forget 'self' here too!
#     def get_average(self):
#         # We need to make sure the list isn't empty before we divide, otherwise Python crashes!
#         if len(self.__grades) == 0:
#             return 0
            
#         total = sum(self.__grades)
#         average = total / len(self.__grades)
#         return average
        
# # --- The Test ---
# # We only pass the name now, because the list starts empty automatically
# obj = Student("ALEX")

# # We add the grades one by one!
# obj.add_grade(85)
# obj.add_grade(90)
# obj.add_grade(105) # This will trigger your error message!

# # Calculate and print the average
# print(f"{obj.name}'s Average: {obj.get_average()}")




class Student:
    def __init__(self, name):
        self.name = name
        # 1. Upgrade to a dictionary to hold Subject: Grade pairs
        self.__grades = {} 

    # We update the single-grade method to require a subject name
    def add_grade(self, subject, grade):
        if 0 <= grade <= 100:
            self.__grades[subject] = grade
            print(f"Added {subject} ({grade}) to {self.name}'s file.")
        else:
            print(f"Error: {grade} is invalid for {subject}.")   

    # 2. The Bulk Method! It takes a whole dictionary at once.
    def add_bulk_grades(self, grades_dictionary):
        print(f"\n--- Processing bulk grades for {self.name} ---")
        # Loop through the dictionary and reuse our single-grade logic!
        for subject, grade in grades_dictionary.items():
            self.add_grade(subject, grade) 

    def get_average(self):
        if len(self.__grades) == 0:
            return 0
        
        # We only want to sum the VALUES (the numbers), not the subject names
        total = sum(self.__grades.values())
        return total / len(self.__grades)

# --- The Test ---
obj = Student("ALEX")

# Instead of calling add_grade 5 times, we pass a dictionary once!
alex_report_card = {
    "Math": 85,
    "Science": 92,
    "History": 78,
    "English": 88,
    "Art": 105 # Still testing our error logic!
}

# Pass the whole dictionary into the bulk method
obj.add_bulk_grades(alex_report_card)

print(f"\n{obj.name}'s Final Average: {obj.get_average()}")