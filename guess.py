from random import randint
from random import choice
from rich.console import Console
from rich import print
from rich.panel import Panel
from rich.progress import track
from time import sleep
from math import log2

console = Console()
STOP_GAME = None


jokes = ['Binary search didn\'t help?', 'What\'s the matter with you?', 'You were close!', 'Ha-ha-ha',
        'You accidentally missed', 'Seriously?', 'Almost']


def hello():
    console.print(Panel('''The rules are quite simple:
[red]The program will decide how many attempts you should give.
We will remind you when the last one remains.
I advise you to use binary search.''', title='Guessing number'), justify='center')
    generate()


def is_valid(value):
    try:
        number = int(value)
        assert 1 <= number <= stop
        return number
    except ValueError:
        console.print(Panel('Don\'t you think you were driving a wrong number?', title='[red]Error'), justify='center')
    except AssertionError:
        console.print(Panel(f'The number must be in the range from [yellow]1[/yellow] \
to [yellow]{stop}[/yellow].', title='[red]Error'), justify='center')


def is_correct_range(value):
    return value.isdigit() and 3 <= int(value)


def is_counter():
    global COUNTER
    COUNTER = round(log2(int(stop)))
    return COUNTER != 0


def generate():
    global GUESS, stop
    console.print('[green] -- [i]We need your number to create the end of the range[/i] -- [/green]')
    stop = input('your range: ')
    if is_correct_range(stop) and is_counter():
        stop = int(stop)
        GUESS = randint(1, stop)
        for _ in track(range(50), description='[green]Processing...'):
            sleep(0.03)
        print(Panel(f'[red]The number is generated![/red] You have selected \
a range from [green]1[/green] to [green]{stop}[/green]! You have {COUNTER} attempts in your pocket.'))
        playing_game()
    else:
        console.print(Panel('Are you sure you entered a number?', title='[red]Error'), justify='center')
        generate()


def playing_game():
    while STOP_GAME != True:
        console.print(f'[green] -- [i]And now can you guess?[/i] -- [/green]')
        user_number = input(f'your number: ')
        if is_valid(user_number):
            conditions(user_number)
        if COUNTER == 0:
            console.print(Panel(f'Unfortunately, you have run out of attempts. It was {GUESS}', title='[red]Defeat'), justify='center')
            ask_continue()
        elif COUNTER == 1:
            console.print(Panel('[red]Be careful! You have one last attempt left[/red]', title='Hint'))


def conditions(user_number):
    global COUNTER
    user_number = int(user_number)
    if user_number > GUESS:
        console.print(Panel(f'{choice(jokes)} your number is [red]bigger[/red] than ours.'))
        COUNTER -= 1
    elif user_number < GUESS:
        console.print(Panel(f'{choice(jokes)} your number is [red]less[/red] than ours.'))
        COUNTER -= 1
    else:
        console.print(Panel('''[blue]Congratulations!
Binary search or is my code so clumsy?
I think the second.''', title='Guessing number'), justify='center')
        ask_continue()


def ask_continue():
    global STOP_GAME
    match console.input('[red]don\'t you want to continue? (+/-) [/red]'):
        case '+':
            generate()
        case '-':
            console.print('[blue](͡° ͜ʖ ͡°) Thanks for playing (͡° ͜ʖ ͡°)', justify='center')
            STOP_GAME = True
        case _:
            console.print(Panel('Did you specify these symbols exactly?', title='[red]Error'), justify='center')
            ask_continue()


if __name__ == '__main__':
    hello()
