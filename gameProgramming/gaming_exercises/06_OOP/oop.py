# Object-Oriented Programming, Johnson Traevon, v0.3

class Person: # Use PascalCase for ClassNames
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def __str__(self):
        return f"Name: {self.name}\nShe is {self.age} years old.\nShe is also {self.weight} pounds in weight\n"

    def classFunction(self):
        print("This is an example class function\n")
        print("It only works when called on an object of that class")
        
person1 = Person("Chika Fujiwara", 16, 142)
person2 = Person("Kaguya Shinomiya", 15, 127)
# print(person1)
# print(person2)

# print("                \a\n")

# if person1.weight > person2.weight:
#     print(f"{person1.name} weighs more than {person2.name}\n")
# elif person1.weight == person2.weight:
#     print(f"{person1.name} weighs the same as {person2.name}.\n")
# else: 
#     print(f"{person2.name} weighs more than {person1.name}.\n")

# print("                     \n")

# if person1.age > person2.age:
#     print(f"{person1.name} is older than {person2.name}!\n")
# elif person1.age == person2.age:
#     print(f"{person1.name} and {person2.name} are the same age!\n")
# else: 
#     print(f"{person2.name} is older than {person1.name}\n")

# person1.classFunction()

# Changing Properties 
print(person1.name)
person1.name = "Chika Fujiwara"
print(person1.name)