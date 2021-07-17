class Team: #Parent/Base class
    def __init__(self, name, origin):
        self.teamName = name
        self.teamOrigin = origin

    def printTeam(self):
        print("The team {} is from {}").format(self.teamName, self.teamOrigin)


class Player(Team): #Child/Derived class
    def __init__(self, name, origin, pName, pPoints):
        Team.__init__(self, name, origin)
        self.playerName = pName
        self.playerPoints = pPoints

    def __str__(self):
        return self.playerName + " from " + self.teamName + " has scored " + str(self.playerPoints)
        #return "String function is called"


player1 = Player("KKR", "Kolkata", "PlayerName1", 50)
print(player1)

player2 = Player("CSK", "Chennai", "PlayerName2", 35)
print(player2)