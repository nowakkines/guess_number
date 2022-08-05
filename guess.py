from random import randint
from rich.console import Console
from rich import print
from rich.panel import Panel
from rich.progress import track
from time import sleep


console = Console()
STOP_GAME = None
COUNTER = 0

def hello():
    console.print(Panel('''[red]The rules are quite simple, you have 5 attempts
we will remind you when the last one remains
i advise you to use binary search.''', title='Guessing number'), justify='center')


def generate():
    global stop, GUESS
    console.print('[green] -- [i]We need your number to create the end of the range[/i] -- [/green]')
    stop = console.input('your range: ')
    if is_correct_range(stop):
        stop = int(stop)
        GUESS = randint(1, stop)
        for n in track(range(50), description='Processing...'):
            sleep(0.03)
        print(f'[red]The number is generated![/red] You have selected a range from 1 to {stop}!\n')
    else:
        print('false')
        generate()


def conditions(user_number):
    global STOP_GAME, COUNTER
    user_number = int(user_number)
    if user_number > GUESS:
        COUNTER += 1
        print(f'[HOT] {GUESS} Oh no, your number is bigger than ours.')
    elif user_number < GUESS:
        COUNTER += 1
        print(f'[COLDY] {GUESS} Oh no, your number is less than ours.')
    else:
        print('''
        *****************************
        *   Congrats! You did it.   *
        *****************************\n''')
        ask_continue()


def playing_game():
    global STOP_GAME
    while STOP_GAME != True:
        user_number = input(f'[green]Enter a number[/green] ')
        if is_valid(user_number):
            conditions(user_number)
        if COUNTER == 5:
            print('[-_-] Unfortunately you couldn\'t :)\n')
            ask_continue()
        elif COUNTER == 4:
            print('[1] You have one last attempt!\n')


def ask_continue():
    global STOP_GAME, GUESS, stop
    match input('[?] Don\'t you want to continue? (+/-) '):
        case '+':
            stop = int(input('Enter the end of range >> '))
            GUESS = randint(1, stop)
            for n in track(range(50), description='Processing...'):
                sleep(0.03)
            print(f'[red]The number is generated![/red] You have selected a range from 1 to {stop}!\n')


        case '-':
            print('[!] Thank your for playing!')
            STOP_GAME = True
        case _:
            print('[!] Upps, you didn\'t enter a number! (+ or -)\n')
            ask_continue()


def is_valid(value):
    try:
        number = int(value)
        assert 1 <= number <= stop, f'[!] A mistake. The number must be in the range from 1 to {stop}.'
        return number
    except ValueError:
        print('Don\'t you think you were driving a wrong number?')
    except AssertionError as Error:
        print(Error)


def is_correct_range(value):
    return value.isdigit()


# hello()
generate()
playing_game()