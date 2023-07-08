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
