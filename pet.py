class Pet:
    def __init__(self, name, type, tricks, health=100, energy=50):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        print(f"{self.name} took a nap and is feeling refreshed.")

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} is eating and feels healthier.")

    def play(self):
        if self.energy >= 10:
            self.energy -= 10
            self.health += 10
            print(f"{self.name} got the zoomies.")
        else:
            print(f"{self.name} is feeling lazy.")

    def noise(self):
        print(f"{self.name} makes a noise.")

class Dog(Pet):
    def __init__(self, name, tricks, health=100, energy=50, breed="unknown"):
        super().__init__(name, "Dog", tricks, health, energy)
        self.breed = breed

    def wag_tail(self):
        print(f"{self.name} wags their tail.")

    def happy_noise(self):
        print("Boof!")

    def angry_noise(self):
        print("Grrrr!")

class Cat(Pet):
    def __init__(self, name, tricks, health=100, energy=50, color="unknown"):
        super().__init__(name, "Cat", tricks, health, energy)
        self.color = color

    def bite(self):
        print(f"{self.name} bit ur hand haha.")
    
    def happy_noise(self):
        print("prrrrrrrrrrrr")

    def angry_noise(self):
        print("ekekekekkeke!")

# Example usage:
if __name__ == "__main__":
    my_dog = Dog("Spoon", ["sit", "roll over", "hands up"], breed="Chihuahua")
    my_cat = Cat("Cavatappi", ["none"], color="Tuxedo")

    my_dog.wag_tail()
    my_cat.bite()

    my_dog.happy_noise()
    my_cat.angry_noise()
