#Simple Number Guessing Game

import random


def decision():
     print("Hello! I have game for you! Do you want to play? [y/n]")
     choose = input()
     if choose == "y":
          play()
     elif choose == "n":
          print("Bye!")
          quit()

def play():
     mysterious_number = random.randint(1, 10)
     guess = int(input("Guess the number: "))
     if guess != mysterious_number:
          print("Wrong!")
     elif guess == mysterious_number:
          print("You win!")

decision()
play()
     
