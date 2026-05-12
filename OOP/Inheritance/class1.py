class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} faz um som genérico."


class Cachorro(Animal):
    def speak(self):
        return f"{self.name} diz: au au!"


class Gato(Animal):
    def speak(self):
        return f"{self.name} diz: miau!"


if __name__ == "__main__":
    dog = Cachorro("Rex")
    cat = Gato("Mimi")

    print(dog.speak())
    print(cat.speak())
