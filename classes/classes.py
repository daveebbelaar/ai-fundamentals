"""
Introduction to Classes and Object-Oriented Programming (OOP) in Python
"""

# --------------------------------------------------------------
# Define a class
# --------------------------------------------------------------


class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am a {self.species}.")


# --------------------------------------------------------------
# Create an instance of the class
# --------------------------------------------------------------

dog = Pet("Buddy", "Dog")
cat = Pet("Whiskers", "Cat")


# --------------------------------------------------------------
# Access the attributes of the instance
# --------------------------------------------------------------

dog.name  # Output: Buddy
dog.species  # Output: Dog


# --------------------------------------------------------------
# Call the method of the instance
# --------------------------------------------------------------

dog.introduce()  # Output: Hello, my name is Buddy and I am a Dog.
cat.introduce()  # Output: Hello, my name is Whiskers and I am a Cat.


# --------------------------------------------------------------
# Update the attributes of the instance
# --------------------------------------------------------------

dog.name = "Max"
dog.color = "Brown"

dog.name  # Output: Max
dog.color  # Output: Brown
