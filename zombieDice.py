'''
    Zombie Dice Bots

    Makes game playing AI's?

    **On each players turn**
    1. Place all 13 dice in a cup. Player randomly draws 3 dice from cup and rolls them.
       Players always roll 3 Dice.
    2.Set aside count up any brains(humans brains who were eaten) and shotguns(humans who
    fought back). Accumulating 3 shotguns automatically ends a player's turn with zero points,(
    regardless of how many brains they had). If they had 0-2 shotguns they can continue rolling
    if they want. They may also choose to end their turn and collect one point per brain.
    3. If the player decides to keep rollign they must reroll all dice with footsteps. Remember
    that the player must always roll 3 dice; they must draw more dice out of the cup if they have 
    fewer than three footsteps to roll. A player may keep rolling dice until either they get three
    shotguns-- losing everythin-- or all 13 dice have been rolled. A player may not reroll only
    one or two dice, and may not stop mid-reroll.
    4. When someone reaches 13 brains, the rest of the players finish out the round. THe person
    with the most brains wins. If there's a tie, the tied players play one last tiebreaker round.

'''
import zombiedice, random

class MyZombie:
    
    def __init__(self,name):
        # all zombies must have a name:
        self.name = name
    def turn(self,gameState):
        # gamestate is a dict with info about the current state of the game
        # You can choose to ignore it in your code
        diceRollResults = zombiedice.roll() #first roll
        # roll() returns a dictionary with keys 'brains','shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color,icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value.
        # {'brains':1,'footsteps':1,'shotgun':1,
        #  'rolls':[('yellow','brains'),('red,'footsteps'),
        #           ('green','shotgun')]}
        #
        #TEST CODE? REPLACE
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains <2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

#A bot that always rolls twice per turn
class AlwaysRollsTwicePerTurn:

    def __init__(self,name):
        self.name = name
    
    def turn(self, gameState):
        zombiedice.roll()
        zombiedice.roll()

#A bot that, after the first roll, randomly decides if it will continue or stop
class RandomyCat:
    def __init__(self,name):
        self.name = name
    def turn(self, gameState):
        zombiedice.roll()
        #randomly decide to stop or continue
        a = 1
        while a == True: 
            zombiedice.roll()
            a = random.randint(0,1)



#A bot that stops rolling after it has rolled two brains
class TwoBrainsAndDone:
    def __init__(self,name):
        self.name = name

    def turn(self,gameState):
        brains = 0
        zombiedice.roll()
        

        


#A bot that stops rolling after it has rolled two shotguns
#A bot that initially decides it’ll roll the dice one to four times, but will stop early if it rolls two shotguns
#A bot that stops rolling after it has rolled more shotguns than brains






#Declare zombie class instances in this tuple
zombies = (
    ## EXAMPLE ZOMBIES ##
    #zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    #zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    #zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    #zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),

    MyZombie(name='My Zombie Bot'),
    AlwaysRollsTwicePerTurn(name='Twicey'),
    RandomyCat(name='Hot Streak?')
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)