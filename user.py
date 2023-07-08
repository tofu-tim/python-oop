class Shoe:
    def __init__(self, brand, shoe_type, price):
        self.brand = brand
        self.type = shoe_type
        self.price = price
        self.in_stock = True

skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
print(skater_shoe.type)
print(dress_shoe.type)

# Ninja Challenges!
# Open this code on the Trace website to get a better view of all the variables and their attributes.
# Make a new instance of a shoe
climbing_shoe = Shoe("Black Diamond", "Climbing Shoe", 74.96)
# Update the in_stock attribute to False

climbing_shoe.in_stock = False

print(climbing_shoe.in_stock)