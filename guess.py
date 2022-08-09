from random import randint
from random import choice
from rich.console import Console
from rich import print
from rich.panel import Panel
from rich.progress import track
from time import sleep

console = Console()
STOP_GAME = None
COUNTER = 0


jokes = ['Binary search didn\'t help?', 'What\'s the matter with you?', 'You were close!', 'Ha-ha-ha',
        'You accidentally missed', 'Seriously?', 'Almost']


def hello():
    console.print(Panel('''[red]The rules are quite simple, you have 5 attempts
we will remind you when the last one remains
i advise you to use binary search.''', title='Guessing number'), justify='center')
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
    return value.isdigit() and 1 <= int(value)


def generate():
    global GUESS, stop
    console.print('[green] -- [i]We need your number to create the end of the range[/i] -- [/green]')
    stop = input('your range: ')
    if is_correct_range(stop):
        stop = int(stop)
        GUESS = randint(1, stop)
        for _ in track(range(50), description='[green]Processing...'):
            sleep(0.03)
        print(Panel(f'[red]The number is generated![/red] You have selected \
a range from [green]1[/green] to [green]{stop}[/green]!'))
        playing_game()
    else:
        console.print(Panel('Are you sure you entered a number?', title='[red]Error'), justify='center')
        generate()


def playing_game():
    while STOP_GAME != True:
        console.print('[green] -- [i]And now can you guess?[/i] -- [/green]')
        user_number = input(f'your number: ')
        if is_valid(user_number):
            conditions(user_number)
        if COUNTER == 5:
            console.print(Panel('Unfortunately, you have run out of attempts.', title='[red]Defeat'))
            ask_continue()
        elif COUNTER == 4:
            console.print(Panel('Be careful! You have [red]one last attempt left[/red]', title='Hint'))


def conditions(user_number):
    global COUNTER
    user_number = int(user_number)
    if user_number > GUESS:
        console.print(Panel(f'{choice(jokes)}, your number is [red]bigger[/red] than ours.'))
        COUNTER += 1
    elif user_number < GUESS:
        console.print(Panel(f'{choice(jokes)}, your number is [red]less[/red] than ours.'))
        COUNTER += 1
    else:
        console.print(Panel('''[blue]Congratulations!
Binary search or is my code so clumsy?
I think the second.''', title='Guessing number'), justify='center')
        ask_continue()


def ask_continue():
    global STOP_GAME
    match console.input('[red]                         Don\'t you want to continue? (+/-) [/red]'):
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
