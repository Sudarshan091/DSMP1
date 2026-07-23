# from abc import ABC,abstractmethod 
# class student(ABC):
#     def name(self,name):
#         self.name=name
#         return name
#         print(name)
#     def course(self):
#         print('200 out of 300 student in uni is enrolled in btech ')
#     @abstractmethod
#     def college(self):
#         print('college is jnct ')
#     @abstractmethod
#     def city(self):
#         print('one and only bhopal ')
# class parent(student):
#     def find_child(self):
#             print('where is my son ')

#     def college(self):
#             print('jnct')

#     def city(self):
#             print('bhopal')
# st1=parent()
# st1.city()
# name=st1.name('sudarshan')
# print(name)



from abc import ABC, abstractmethod 

# 1. Capitalized class names to follow Python conventions (PascalCase)
class Student(ABC):
    
    # 2. Changed method name to 'set_name' to avoid overwriting the method with the variable
    def set_name(self, student_name):
        self.name = student_name
        return self.name
        # Note: The print statement here was removed because 'return' exits the function immediately.
        
    def course(self):
        print('200 out of 300 students in the uni are enrolled in BTech.')
        
    @abstractmethod
    def college(self):
        # 3. Used 'pass' because abstract methods are meant to be empty blueprints
        pass 
        
    @abstractmethod
    def city(self):
        pass

# Inheriting from the abstract Student class
class Parent(Student):
    def find_child(self):
        print('Where is my son?')

    # 4. Providing the concrete implementation for the abstract methods
    def college(self):
        print('JNCT')

    def city(self):
        print('Bhopal')

# --- Implementation Instructions ---
# 1. Create an instance of the concrete class (Parent)
st1 = Parent()

# 2. Call the implemented abstract method
st1.city()

# 3. Call the inherited and renamed set_name method
student_name = st1.set_name('Sudarshan')
print(student_name)