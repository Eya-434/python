

#challenge 1
class Player:
    def __init__(self, display_player_info):
        self.name = display_player_info["name"]
        self.age = display_player_info["age"]
        self.position = display_player_info["position"]
        self.team = display_player_info["team"]

#challenge 2
Kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}
Jason = {"name": "Jason Tatum", "age":24, "position": "small forward", "team": "Boston Celtics"}
Kyrie = {"name": "Kyrie Irving", "age":32, "position": "Point Guard", "team": "Brooklyn Nets"}

player1 = Player(Kevin)
player2 = Player(Jason)
player3 = Player(Kyrie)


#challenge 3
new_team = [player1, player2, player3]

for player in new_team :
    print(f"{player.name} , {player.age }, {player.position}, {player.team}")

