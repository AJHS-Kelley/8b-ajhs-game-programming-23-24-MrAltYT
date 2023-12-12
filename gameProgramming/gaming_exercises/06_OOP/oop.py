# Object-Oriented Programming, Johnson Traevon, v0.1

class Person: # Use PascalCase for ClassNames
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def __str__(self):
        return f"Name: {self.name}\nShe is {self.age} years old.\nShe is also {self.weight} pounds in weight"


person1 = Person("Chika Fujiwara", 16, 132)
print(person1)




