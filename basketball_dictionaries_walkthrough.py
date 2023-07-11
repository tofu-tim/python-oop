class Player:
    def __init__(self, player_info):
        self.name = player_info["name"]
        self.age = player_info["age"]
        self.position = player_info["position"]
        self.team = player_info["team"]

    def __repr__(self):
        return "Player: {}, {} y/o, position: {}, team: {}".format(
            self.name, self.age, self.position, self.team)

kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}


player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

print(player_kevin)