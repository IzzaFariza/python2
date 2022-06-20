#!/usr/bin/env python

import random

def main():
    """Start a Periodic Table game."""
    print("Guess the elements : Alkali Metals!")

    alkali = [
        "lithium",
        "sodium",
        "potassium",
        "rubidium",
        "caesium",
        "francium",
        ]

    x = random.choice(alkali)
    
    guess = None

    while x != guess:

        guess = str(input("What alkali metals am I thinking of? "))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))

main()