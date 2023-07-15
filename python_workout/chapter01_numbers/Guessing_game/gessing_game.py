# usr/bin/python3
import random

"""
1. Write a function (guessing_game) that takes no arguments. 
2. When run, the function chooses a random integer between 0 and 100 (inclusive).
3. Then ask the user to guess what number has been chosen.
4. Each time the user enters a guess, the program indicates one of the following:
    - too low 
    - too high
    - just right!
5. If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.
6. The program only exits after the user guesses correctly.

EXTRA:
7. Modify this program, such that it gives the user only three chances to guess the
correct number. If they try three times without success, the program tells them
that they didn’t guess in time and then exits.

8. 
"""

def guessing_game():
    
    MIN_VALUE = 0
    MAX_VALUE = 100
    
    answer = random.randint(MIN_VALUE, MAX_VALUE)

    count = 0

    while player_guess := input("enter a number between 1 to 100: "):
            player_guess = int(player_guess)
            if count >= 3:
                print("Sorry, your out of luck")
                break    
            if player_guess == answer:
                print(f"Right! the answer is {player_guess}")
                break
                
            elif player_guess > answer:
                print(f"The answer is lower than {player_guess}")

            elif player_guess < answer:
                print(f"The answer is higher than {player_guess}")
                
            elif count >= 3:
                print("Sorry, your out of luck")
                break
            count += 1

if __name__ == "__main__":
    guessing_game()