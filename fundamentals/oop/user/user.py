class User:		
    def __init__(self,first_name, last_name , email , age):
        self.first_name = first_name
        self.last_name=last_name
        self.email = email
        self.age= age
        self.is_rewards_member = False
        self.gold_card_points= 0
    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name : {self.last_name}")
        print(f"Email : {self.email}")
        print(f"Age : {self.age}")
        print(f"Reward Member : {self.is_rewards_member}")
        print(f"Gold Card Points : {self.gold_card_points}")
    def enroll(self):
        self.is_rewards_member= True
        self.gold_card_points=200
    def spend_points(self, points):
        if self.gold_card_points>=points:
            self.gold_card_points -= points
        else : print(f" not enough points!{self.gold_card_points}")


user1 = User("jon" , "doe","jon@.com",25)
user2=User("eya","zarrad","eya@.com", 22)
user1.enroll()
user1.spend_points(50)
user1.display_info()
user2.display_info()
user2.spend_points(50)
