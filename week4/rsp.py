# Game Rock/Sissors/Paper
import random as rd
playing = True
while playing:
    # ask user to choose rock, sissors or paper
    user_choice = input("Please choose rock, sissors or paper: ")

    if user_choice not in ['rock', 'sissors', 'paper']:
        print('Invalid choice. Must be rock, sissors or paper')
    else:
        # generate random number for computer (1 for rock, 2 for sissors, 3 for paper)
        computer_choice = rd.randint(1, 3)
        computer_choice = 'rock' if computer_choice == 1 else \
                          'sissors' if computer_choice == 2 else 'paper'
        print('Computer choice: ', computer_choice)
        # compare user input and computer number to decide a winner
        if user_choice == computer_choice:
            print('Draw')
        elif (user_choice == 'rock'    and computer_choice == 'sissors') or \
             (user_choice == 'sissors' and computer_choice == 'paper')   or \
             (user_choice == 'paper'   and computer_choice == 'rock'):
            print('You win')
        else:
            print('You lose')

        answer = input('Do you want to play again? (y/n): ')
        playing = answer == 'y'