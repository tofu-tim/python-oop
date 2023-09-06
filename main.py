from pet import Pet
from ninja import Ninja

if __name__ == "__main__":
    my_pet = Pet("Spoon", "Dog", ["sit", "roll over", "shake", "stay"])
    my_ninja = Ninja("Thomas", "Aquinas", treats=5, pet_food=10, pet=my_pet)

    my_ninja.walk()
    my_ninja.feed()
    my_ninja.bathe()
    my_pet.sleep()

