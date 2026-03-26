import random
import time

def print_dramatic_text(text: str, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    print_dramatic_text('welcome to rock, paper, scissors! 🗿📃✂️')

    options = ['rock', 'paper', 'scissors']

    score = 0

    i = 0
    while i < 3:

        player = input('please enter rock, paper or scissors: ')

        r = random.randint(0, 2)

        computer = options[r]

        if player == computer:
            print_dramatic_text(f'you chose {player}, computer chose {computer} ... you tie!')

        if player == 'rock' and computer == 'scissors':
            print_dramatic_text(f'you chose {player}, computer chose {computer} ... you win!')

        if player == 'rock' and computer == 'paper':
            print_dramatic_text(f'you chose {player}, computer chose {computer}... lol u lost!')

        if player == 'scissors' and computer == 'paper':
            print_dramatic_text(f'you chose {player}, computer chose {computer} you won!!')
            score += 1

        if player == 'scissors' and computer == 'rock':  
            print_dramatic_text(f'you chose {player}, computer chose {computer} you lose :( )')

        if player == 'paper' and computer == 'rock':    
            print_dramatic_text(f'you chose {player}, computer chose {computer} you won !!)')
            score += 1 

        if player == 'paper' and computer == 'scissors':    
            print_dramatic_text(f'you chose {player}, computer chose {computer} you lose :( oh no ))')

        i += 1

    print(f'congrats!! you scored {score}/3!')
