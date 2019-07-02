import random

class UserPlayer:
    """ Class to represent the players"""

    def __init__ (self):
        """ Initialize the players """
        self.score = 0

    def turn(self, die):
        turn_score = 0
        keep_rolling = True
        while keep_rolling:
            rolled_value = die.roll()
            turn_score += rolled_value
            if rolled_value == 1:
                print("You rolled a :pig:")
                turn_score = 0
                break
            print(f'You rolled {rolled_value}. Your round score {turn_score}')
            ask_user = input("Choose (h) to hold or (k) to keep playing:  ").lower()
            if ask_user == 'h':
                keep_rolling = False
            
        self.score += turn_score
        print(f"Your total score is {self.score}")
        return 
       
          

class ComputerPlayer:

    def __init__ (self):
        """ Initialize the players """
        self.score = 0

    def turn(self, die):
        turn_score = 0
        while turn_score < 20:
            rolled_value = die.roll()
            if rolled_value == 1:
                print("Computer rolled a :pig:")
                turn_score = 0
                return 
            else: 
                turn_score += rolled_value
                print(f'Computer rolled {rolled_value}. Computer round score {turn_score}')
        self.score += turn_score
        print(f"Computer total score is {self.score}")
        return


    
class Die:
    """ Class representing the dice """
    
    def __init__(self, sides=6):
        """ Initializes dice class"""
        self.sides = sides
        # self.roll = roll
        

    def roll(self):
        """ Use random to roll dice. Return number from (1,6)""" 
        return random.randint(1, self.sides)
      



class Game:
    """ Class representing the game """

    def __init__ (self):
        self.player1 = None
        self.player2 = None
        

    def toss_coin(self):
        user_player = UserPlayer()
        computer_player = ComputerPlayer()
        
        user_input = input("Choose 'heads' or 'tails' to begin the game:  ").lower()
       
        coin_flip = random.randint(0,1)
        if user_input == "heads":
            user_input = 1
        elif user_input == 'tails':
            user_input = 0
        if user_input == coin_flip:
            self.player1 = user_player 
            self.player2 = computer_player
            print("You start the game.")

        else:
            self.player1 = computer_player
            self.player2 = user_player
            print("Wait your turn.")

        return self.player1, self.player2
    
    def play(self):
        player1, player2 = self.toss_coin()
        die = Die()
       

        while player1.score != 100 and player2.score != 100:
            player1.turn(die)
            player2.turn(die)
        if player1.score >= 100:
            print(f"{player1} is the winner")
        else: 
            print(f"{player2} is the winner")
    

game = Game()
game.play()