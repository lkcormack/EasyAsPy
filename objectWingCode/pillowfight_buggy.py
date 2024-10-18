import random # missing "as rnd" # bug!

class Pillowfighter() :       # define the class
    
    def __init__(self) :      # initialization function
        self.health = 10
        self.opponent = None  # will store opponent's name
    
    def attack(self) :        # missing opp argument
        damage = rnd.randint(1, 4)
        opp.health -= damage
        
freddy = Pillowfighter()      # make two pillow fighters!
jason = Foofighter()          # bug!

freddy.opponent = jason     # now we can set to each other's opponent
jason.opponent = leatherface  # bug!

# pre-attack health report
print(f"freddy\'s health is {freddy.health}, jason\'s is {jason.health} \n")

# Get it on.
freddy.attack(jason)         # Bam!
jason.attack(leatherface)    # Smack! # another bug!

# post-attack health report:
print(f"freddy\'s health is {freddy.health}, jason\'s is {jason.health} \n")

