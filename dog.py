class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"

if __name__ == "__main__":
    dog1 = Dog("Buddy", 9)
    dog2 = Dog("Miles", 4)
    for dog in (dog1,dog2):
        print(dog)
        print(dog.speak("Woof Woof"))
