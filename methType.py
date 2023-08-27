# Instance Method 

# class Person:
#     def __init__(self,name):
#         self.name = name
#     def greet(self):
#         print(f"Hello! {self.name}")

# per = Person("Rohit")
# per.greet()


# Class Method

class Person:
    @classmethod
    def classMeth(cls):
        print(f"Hello!")

Person.classMeth()