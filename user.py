class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("First name: " + self.first_name)
        print("Last name: " + self.last_name)
        print("Email: " + self.email)
        print("Age: " + str(self.age))
        if self.is_rewards_member == False:
            print("Rewards member status: inactive")
        else:
            print("Rewards member status: Active")
            print("Gold Card points: " + str(self.gold_card_points))
    
    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print("Insufficient points.")
        else:
            self.gold_card_points -= amount
        return self.gold_card_points


user1 = User("John", "Doe", "jdiddy@gmail.com", 10)
user2 = User("Joe", "Biden", "jbiddy@gmail.gov", 100)
user3 = User("Jackie", "Chan", "jchan@gmail.info", 20)

user1.display_info().enroll().spend_points(50).display_info()
user2.enroll().spend_points(80).display_info()

user1.enroll()

user3.spend_points(10)
