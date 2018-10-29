# -*- coding: utf-8 -*-
"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
GOING FOR EXCEEDS
---------------------------------
@author: bg
"""
import random

LOW_VALUE = 1
HIGH_VALUE = 10
LINE_LENGTH = 35


def play_games():
    """
    Play one or more guessing games.  
    """   
    
    # Display welcome banner.
    welcome_banner()
    
    # Play game
    best = None
    will_play = True
    while (will_play):    
        will_play, best = play_a_game(best)
            
    # Display concluding banner
    farewell_banner() 
 

#import pdb
def play_a_game(best):
    """
    Play one guessing game.
    """
            
    # Initialize the game parameters.
    valid = calculate_range(LOW_VALUE, HIGH_VALUE)
    secret = secret_number(valid)

    report_best_score(best)
        
    tries = 1
    while True:
        
        #pdb.set_trace()
            
        print("\nTry #{}".format(tries))
        guess = input(
                "Pick a number between {} and {}:  ".format
                (LOW_VALUE, HIGH_VALUE)
                )            
        try:
            guess = validate_guess(guess, valid)
        except ValueError as err:
            print("Oh no!  That's not a valid value.  Try again...")
            print("({})".format(err))
        else:
            chk = check_guess(guess, secret)
            if chk:
                break
            valid.remove(guess)          
            tries += 1
    print("You got it!  It took {} tries.".format(tries)) 
    return play_again(), update_best_count(tries, best)


def validate_guess(guess, valid):
    """
    Convert into integer.
    Determine if guess is valid.
    Raise error if cannot be converted or guess out of 
    valid values.
    """
    guess = int(guess)
    if guess not in valid:
        raise ValueError("Guess either out of range or guessed before")
    return guess


def check_guess(guess, secret_number):
    "Is guess higer or lower than secret number?"     
    if guess < secret_number:
        print("It is HIGHER!")
        return False
    elif guess > secret_number:
        print("It is LOWER!")
        return False
    return True


def play_again():
    "Determine if user wishes to play again."
    response = input("Play again [Y]es or [N]o?  ").lower()
    if response[0]=="y":
        print("Replaying...")
        return True
    return False
           

def calculate_range(low, high):
    "Determine all possible guesses"
    return list(range(low, high+1))


def secret_number(valid):
    "Determine secret number for one game"
    return random.sample(valid, 1)[0]
    

def print_line(num):
    "Print a certain number of dashes"
    print(num*'-')


def welcome_banner():
    "Print welcome message"
    print()
    print_line(LINE_LENGTH)
    print("Welcome to the Number Guessing Game")
    print_line(LINE_LENGTH)
    

def farewell_banner():
    "Print concluding message"
    print()
    print_line(LINE_LENGTH)
    print("Closing game, see you next time!")
    print_line(LINE_LENGTH)
    

def report_best_score(count):
    "Report best score in terms of minimum count"
    if count!=None:
        print("\nThe BEST SCORE is {}.".format(count))
        

def update_best_count(count, best_count):
    """
    Calculate the best minimum count using previous and
    current best.
    """
    if best_count==None:
        return count
    if count < best_count:
        return count
    return best_count
    
    
if __name__=="__main__":
    play_games()
