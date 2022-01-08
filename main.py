import random
import art
import game_data
import os

def clrscr():
    # Check if Operating System is Mac and Linux or Windows
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # Else Operating System is Windows (os.name = nt)
      _ = os.system('cls')

new_game = True

while new_game == True:

    game_playing = True

    score = 0

    A = random.choice(game_data.data)
    game_data.data.remove(A)

    print(art.logo)

    while game_playing == True:

        B = random.choice(game_data.data)
        game_data.data.remove(B)

        print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")

        print(art.vs)

        print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}.")

        if A['follower_count'] > B['follower_count']:
            answer = 'a'
            loop_answer = A
        else:
            answer = 'b'
            loop_answer = B

        guess = input("Who has more followers? Type 'A' or 'B': ").strip().lower()

        if answer == guess:
            score += 1
            A = loop_answer
            clrscr()
            print(art.logo)
            print(f"You are correct! Current score: {score}")
        
        else:
            clrscr()
            print(f"You lose! You scored a {score}")
            game_playing = False
    
    play_again = input("Would you like to play again? Type 'Yes' or 'No': ").strip().lower()
    if play_again == 'no':
        new_game = False
    else:
        clrscr()

input()