from pet import Pet

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    

    def walk(self):
        self.pet.play()
        print(f"{self.first_name} walks {self.pet.name}.")

    def feed(self):
        if self.treats > 0:
            self.treats -= 1
            print(f"{self.first_name} feeds {self.pet.name}.")
            self.pet.eat()
        else:
            print(f"{self.first_name} is out of treats.")

    def bathe(self):
        self.pet.noise()
        print(f"{self.first_name} bathes {self.pet.name}. {self.pet.name} is all clean!")
